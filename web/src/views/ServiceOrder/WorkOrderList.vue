<!-- src/views/ServiceOrder/WorkOrderList.vue -->
<template>
  <div class="work-order-list">
    <h2>工单管理</h2>
    <DataTable
      :data="workOrders"
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

const workOrders = ref([]);

const tableColumns = [
  { prop: 'id', label: 'ID' },
  { prop: 'title', label: '标题' },
  { prop: 'customer.name', label: '客户', formatter: (row) => row.customer?.name || '-' },
  { prop: 'priority', label: '优先级', formatter: (row) => ({1: '低', 2: '中', 3: '高', 4: '紧急'})[row.priority] || '未知' },
  { prop: 'status', label: '状态', formatter: (row) => ({'pending': '待处理', 'assigned': '已分配', 'in_progress': '处理中', 'completed': '已完成', 'closed': '已关闭'})[row.status] || '未知' },
  { prop: 'assigned_to.profile.user.first_name', label: '指派给', formatter: (row) => row.assigned_to?.profile?.user?.first_name || '-' },
  { prop: 'created_at', label: '创建时间' },
];

onMounted(() => {
  loadWorkOrders();
});

const loadWorkOrders = async () => {
  try {
    // const response = await apiClient.get('/workorders/');
    // workOrders.value = response.data.results;
    // 模拟数据
    workOrders.value = [
      { id: 1, title: '服务器宕机', customer: { name: 'ABC公司' }, priority: 4, status: 'in_progress', assigned_to: { profile: { user: { first_name: '张' }}}, created_at: '2023-10-27T10:00:00Z' },
      { id: 2, title: '新功能咨询', customer: { name: 'XYZ公司' }, priority: 2, status: 'pending', assigned_to: null, created_at: '2023-10-28T11:00:00Z' },
    ];
  } catch (error) {
    console.error('Failed to fetch work orders:', error);
    ElMessage.error('获取工单列表失败');
  }
};

const handleAdd = () => {
  ElMessage.info('前往新增工单页面');
};

const handleEdit = (row) => {
  ElMessage.info(`编辑工单: ${row.title}`);
};

const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm(`确定要删除工单 "${row.title}" 吗？`, '警告', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    });
    // await apiClient.delete(`/workorders/${row.id}/`);
    workOrders.value = workOrders.value.filter(w => w.id !== row.id);
    ElMessage.success('删除成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败');
    }
  }
};
</script>

<style scoped>
.work-order-list {
  padding: 20px;
}
</style>