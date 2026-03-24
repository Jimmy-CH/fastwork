<!-- src/views/Accounts/RoleList.vue -->
<template>
  <div class="role-list">
    <h2>角色管理</h2>
    <DataTable
      :data="roles"
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

const roles = ref([]);

const tableColumns = [
  { prop: 'id', label: 'ID' },
  { prop: 'name', label: '角色名称' },
  { prop: 'description', label: '描述' },
  { prop: 'permissions', label: '权限', formatter: (row) => row.permissions.join(', ') },
];

onMounted(() => {
  loadRoles();
});

const loadRoles = async () => {
  try {
    // const response = await apiClient.get('/roles/');
    // roles.value = response.data.results;
    // 模拟数据
    roles.value = [
      { id: 1, name: '管理员', description: '拥有最高权限', permissions: ['admin'] },
      { id: 2, name: '销售', description: '销售相关权限', permissions: ['view_customer', 'create_quotation'] },
    ];
  } catch (error) {
    console.error('Failed to fetch roles:', error);
    ElMessage.error('获取角色列表失败');
  }
};

const handleAdd = () => {
  ElMessage.info('前往新增角色页面');
};

const handleEdit = (row) => {
  ElMessage.info(`编辑角色: ${row.name}`);
};

const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm(`确定要删除角色 "${row.name}" 吗？`, '警告', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    });
    // await apiClient.delete(`/roles/${row.id}/`);
    roles.value = roles.value.filter(r => r.id !== row.id);
    ElMessage.success('删除成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败');
    }
  }
};
</script>

<style scoped>
.role-list {
  padding: 20px;
}
</style>