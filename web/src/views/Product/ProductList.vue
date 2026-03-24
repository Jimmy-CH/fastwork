<!-- src/views/Product/ProductList.vue -->
<template>
  <div class="product-list">
    <h2>产品管理</h2>
    <DataTable
      :data="products"
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

const products = ref([]);

const tableColumns = [
  { prop: 'id', label: 'ID' },
  { prop: 'name', label: '名称' },
  { prop: 'code', label: '编码' },
  { prop: 'category.name', label: '分类', formatter: (row) => row.category?.name || '-' },
  { prop: 'unit_price', label: '单价', formatter: (row) => `¥${row.unit_price}` },
  { prop: 'cost_price', label: '成本价', formatter: (row) => `¥${row.cost_price}` },
  { prop: 'unit', label: '单位' },
  { prop: 'min_stock', label: '最低库存' },
  { prop: 'created_at', label: '创建时间' },
];

onMounted(() => {
  loadProducts();
});

const loadProducts = async () => {
  try {
    // const response = await apiClient.get('/products/');
    // products.value = response.data.results;
    // 模拟数据
    products.value = [
      { id: 1, name: '高性能服务器', code: 'SERV-001', category: { name: '硬件' }, unit_price: 15000.00, cost_price: 12000.00, unit: '台', min_stock: 5, created_at: '2023-10-26T09:00:00Z' },
      { id: 2, name: '云服务套餐', code: 'CLOUD-001', category: { name: '服务' }, unit_price: 99.00, cost_price: 50.00, unit: '月', min_stock: 0, created_at: '2023-10-26T09:05:00Z' },
    ];
  } catch (error) {
    console.error('Failed to fetch products:', error);
    ElMessage.error('获取产品列表失败');
  }
};

const handleAdd = () => {
  ElMessage.info('前往新增产品页面');
};

const handleEdit = (row) => {
  ElMessage.info(`编辑产品: ${row.name}`);
};

const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm(`确定要删除产品 "${row.name}" 吗？`, '警告', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    });
    // await apiClient.delete(`/products/${row.id}/`);
    products.value = products.value.filter(p => p.id !== row.id);
    ElMessage.success('删除成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败');
    }
  }
};
</script>

<style scoped>
.product-list {
  padding: 20px;
}
</style>