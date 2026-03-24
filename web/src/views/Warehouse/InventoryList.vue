<!-- src/views/Warehouse/InventoryList.vue -->
<template>
  <div class="inventory-list">
    <h2>库存管理</h2>
    <DataTable
      :data="inventories"
      :columns="tableColumns"
      @add="handleAdd"
      @edit="handleEdit"
      @delete="handleDelete"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import DataTable from '@/components/Common/DataTable.vue';
import { ElMessage, ElMessageBox } from 'element-plus';
import apiClient from '@/api';

const inventories = ref([]);

const tableColumns = [
  { prop: 'id', label: 'ID' },
  { prop: 'product.name', label: '产品', formatter: (row) => row.product?.name || '-' },
  { prop: 'quantity_on_hand', label: '现有库存' },
  { prop: 'quantity_reserved', label: '已预留' },
  { prop: 'quantity_available', label: '可用库存', formatter: (row) => row.quantity_on_hand - row.quantity_reserved },
  { prop: 'last_updated', label: '最后更新' },
];

onMounted(() => {
  loadInventories();
});

const loadInventories = async () => {
  try {
    // const response = await apiClient.get('/inventory/');
    // inventories.value = response.data.results;
    // 模拟数据
    inventories.value = [
      { id: 1, product: { name: '高性能服务器' }, quantity_on_hand: 50, quantity_reserved: 10, last_updated: '2023-10-30T10:00:00Z' },
      { id: 2, product: { name: '云服务套餐' }, quantity_on_hand: 1000, quantity_reserved: 50, last_updated: '2023-10-30T11:00:00Z' },
    ];
  } catch (error) {
    console.error('Failed to fetch inventories:', error);
    ElMessage.error('获取库存列表失败');
  }
};

const handleAdd = () => {
  ElMessage.info('前往新增库存页面');
};

const handleEdit = (row) => {
  ElMessage.info(`编辑库存: ${row.product.name}`);
};

const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm(`确定要删除库存记录吗？`, '警告', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    });
    // await apiClient.delete(`/inventory/${row.id}/`);
    inventories.value = inventories.value.filter(i => i.id !== row.id);
    ElMessage.success('删除成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败');
    }
  }
};
</script>

<style scoped>
.inventory-list {
  padding: 20px;
}
</style>