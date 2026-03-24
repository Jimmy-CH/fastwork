<!-- src/views/Accounts/DepartmentList.vue -->
<template>
  <div class="department-list">
    <h2>部门管理</h2>
    <DataTable
      :data="departments"
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

const departments = ref([]);

const tableColumns = [
  { prop: 'id', label: 'ID' },
  { prop: 'name', label: '部门名称' },
  { prop: 'description', label: '描述' },
];

onMounted(() => {
  loadDepartments();
});

const loadDepartments = async () => {
  try {
    // const response = await apiClient.get('/departments/');
    // departments.value = response.data.results;
    // 模拟数据
    departments.value = [
      { id: 1, name: '销售部', description: '负责销售工作' },
      { id: 2, name: '技术部', description: '负责技术开发' },
    ];
  } catch (error) {
    console.error('Failed to fetch departments:', error);
    ElMessage.error('获取部门列表失败');
  }
};

const handleAdd = () => {
  ElMessage.info('前往新增部门页面');
};

const handleEdit = (row) => {
  ElMessage.info(`编辑部门: ${row.name}`);
};

const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm(`确定要删除部门 "${row.name}" 吗？`, '警告', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    });
    // await apiClient.delete(`/departments/${row.id}/`);
    departments.value = departments.value.filter(d => d.id !== row.id);
    ElMessage.success('删除成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败');
    }
  }
};
</script>

<style scoped>
.department-list {
  padding: 20px;
}
</style>