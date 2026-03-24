<!-- src/views/Product/CategoryList.vue -->
<template>
  <div class="category-list">
    <h2>产品分类</h2>
    <DataTable
      :data="categories"
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

const categories = ref([]);

const tableColumns = [
  { prop: 'id', label: 'ID' },
  { prop: 'name', label: '分类名称' },
  { prop: 'description', label: '描述' },
];

onMounted(() => {
  loadCategories();
});

const loadCategories = async () => {
  try {
    // const response = await apiClient.get('/product-categories/');
    // categories.value = response.data.results;
    // 模拟数据
    categories.value = [
      { id: 1, name: '软件', description: '各类软件产品' },
      { id: 2, name: '硬件', description: '各类硬件设备' },
      { id: 3, name: '服务', description: '各类服务套餐' },
    ];
  } catch (error) {
    console.error('Failed to fetch categories:', error);
    ElMessage.error('获取分类列表失败');
  }
};

const handleAdd = () => {
  ElMessage.info('前往新增分类页面');
};

const handleEdit = (row) => {
  ElMessage.info(`编辑分类: ${row.name}`);
};

const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm(`确定要删除分类 "${row.name}" 吗？`, '警告', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    });
    // await apiClient.delete(`/product-categories/${row.id}/`);
    categories.value = categories.value.filter(c => c.id !== row.id);
    ElMessage.success('删除成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败');
    }
  }
};
</script>

<style scoped>
.category-list {
  padding: 20px;
}
</style>