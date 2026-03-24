<!-- src/views/Accounts/UserList.vue -->
<template>
  <div class="user-list">
    <h2>用户管理</h2>
    <DataTable
      :data="users"
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

const users = ref([]);

const tableColumns = [
  { prop: 'id', label: 'ID' },
  { prop: 'username', label: '用户名' },
  { prop: 'first_name', label: '名' },
  { prop: 'last_name', label: '姓' },
  { prop: 'email', label: '邮箱' },
  { prop: 'is_active', label: '状态', formatter: (row) => row.is_active ? '激活' : '禁用' },
  { prop: 'date_joined', label: '加入日期' },
  { prop: 'profile.department.name', label: '部门', formatter: (row) => row.profile?.department?.name || '-' },
  { prop: 'profile.role.name', label: '角色', formatter: (row) => row.profile?.role?.name || '-' },
];

onMounted(() => {
  loadUsers();
});

const loadUsers = async () => {
  try {
    // const response = await apiClient.get('/users/');
    // users.value = response.data.results;
    // 模拟数据
    users.value = [
      { id: 1, username: 'john_doe', first_name: 'John', last_name: 'Doe', email: 'john@example.com', is_active: true, date_joined: '2023-01-15T10:00:00Z', profile: { department: { name: '销售部' }, role: { name: '销售' } } },
      { id: 2, username: 'jane_smith', first_name: 'Jane', last_name: 'Smith', email: 'jane@example.com', is_active: true, date_joined: '2023-02-20T11:30:00Z', profile: { department: { name: '技术部' }, role: { name: '技术' } } },
    ];
  } catch (error) {
    console.error('Failed to fetch users:', error);
    ElMessage.error('获取用户列表失败');
  }
};

const handleAdd = () => {
  ElMessage.info('前往新增用户页面');
};

const handleEdit = (row) => {
  ElMessage.info(`编辑用户: ${row.username}`);
};

const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm(`确定要删除用户 "${row.username}" 吗？`, '警告', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    });
    // await apiClient.delete(`/users/${row.id}/`);
    users.value = users.value.filter(u => u.id !== row.id);
    ElMessage.success('删除成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败');
    }
  }
};
</script>

<style scoped>
.user-list {
  padding: 20px;
}
</style>