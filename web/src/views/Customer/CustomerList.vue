<!-- src/views/Customer/CustomerList.vue -->
<template>
  <div class="customer-list">
    <h2>客户管理</h2>
    <DataTable
      :data="customers"
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

const customers = ref([]);

const tableColumns = [
  { prop: 'id', label: 'ID' },
  { prop: 'name', label: '客户名称' },
  { prop: 'type', label: '客户类型', formatter: (row) => ({'individual': '个人', 'enterprise': '企业'})[row.type] || '未知' },
  { prop: 'contact_person', label: '联系人' },
  { prop: 'phone', label: '电话' },
  { prop: 'email', label: '邮箱' },
  { prop: 'address', label: '地址' },
  { prop: 'level', label: '客户等级' },
  { prop: 'credit_score', label: '信用分' },
  { prop: 'created_at', label: '创建时间' },
];

onMounted(() => {
  loadCustomers();
});

const loadCustomers = async () => {
  try {
    // const response = await apiClient.get('/customers/');
    // customers.value = response.data.results;
    // 模拟数据
    customers.value = [
      { id: 1, name: '腾讯科技有限公司', type: 'enterprise', contact_person: '张三', phone: '13800138000', email: 'zhangsan@tencent.com', address: '深圳市南山区', level: 'VIP', credit_score: 95, created_at: '2023-10-25T08:00:00Z' },
      { id: 2, name: '李四', type: 'individual', contact_person: '李四', phone: '13900139000', email: 'lisi@example.com', address: '北京市朝阳区', level: '普通', credit_score: 80, created_at: '2023-10-25T08:05:00Z' },
    ];
  } catch (error) {
    console.error('Failed to fetch customers:', error);
    ElMessage.error('获取客户列表失败');
  }
};

const handleAdd = () => {
  ElMessage.info('前往新增客户页面');
};

const handleEdit = (row) => {
  ElMessage.info(`编辑客户: ${row.name}`);
};

const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm(`确定要删除客户 "${row.name}" 吗？`, '警告', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    });
    // await apiClient.delete(`/customers/${row.id}/`);
    customers.value = customers.value.filter(c => c.id !== row.id);
    ElMessage.success('删除成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败');
    }
  }
};
</script>

<style scoped>
.customer-list {
  padding: 20px;
}
</style>