<!-- src/views/Product/BOMList.vue -->
<template>
  <div class="bom-list">
    <h2>BOM清单</h2>
    <DataTable
      :data="boms"
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

const boms = ref([]);

const tableColumns = [
  { prop: 'id', label: 'ID' },
  { prop: 'product.name', label: '主产品', formatter: (row) => row.product?.name || '-' },
  { prop: 'component.name', label: '组件', formatter: (row) => row.component?.name || '-' },
  { prop: 'quantity', label: '数量' },
];

onMounted(() => {
  loadBOMs();
});

const loadBOMs = async () => {
  try {
    // const response = await apiClient.get('/boms/');
    // boms.value = response.data.results;
    // 模拟数据
    boms.value = [
      { id: 1, product: { name: '高性能服务器' }, component: { name: 'CPU' }, quantity: 2 },
      { id: 2, product: { name: '高性能服务器' }, component: { name: '内存条' }, quantity: 8 },
    ];
  } catch (error) {
    console.error('Failed to fetch BOMs:', error);
    ElMessage.error('获取BOM列表失败');
  }
};

const handleAdd = () => {
  ElMessage.info('前往新增BOM页面');
};

const handleEdit = (row) => {
  ElMessage.info(`编辑BOM ID: ${row.id}`);
};

const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm(`确定要删除BOM记录吗？`, '警告', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    });
    // await apiClient.delete(`/boms/${row.id}/`);
    boms.value = boms.value.filter(b => b.id !== row.id);
    ElMessage.success('删除成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败');
    }
  }
};
</script>

<style scoped>
.bom-list {
  padding: 20px;
}
</style>