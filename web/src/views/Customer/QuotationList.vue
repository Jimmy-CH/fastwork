<!-- src/views/Customer/QuotationList.vue -->
<template>
  <div class="quotation-list">
    <h2>报价单管理</h2>
    <DataTable
      :data="quotations"
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

const quotations = ref([]);

const tableColumns = [
  { prop: 'id', label: 'ID' },
  { prop: 'title', label: '标题' },
  { prop: 'customer.name', label: '客户', formatter: (row) => row.customer?.name || '-' },
  { prop: 'total_amount', label: '总金额', formatter: (row) => `¥${row.total_amount.toFixed(2)}` },
  { prop: 'status', label: '状态', formatter: (row) => ({'draft': '草稿', 'sent': '已发送', 'confirmed': '已确认', 'rejected': '已拒绝'})[row.status] || '未知' },
  { prop: 'created_at', label: '创建时间' },
];

onMounted(() => {
  loadQuotations();
});

const loadQuotations = async () => {
  try {
    // const response = await apiClient.get('/quotations/');
    // quotations.value = response.data.results;
    // 模拟数据
    quotations.value = [
      { id: 1, title: '服务器采购方案', customer: { name: '腾讯科技有限公司' }, total_amount: 150000.00, status: 'confirmed', created_at: '2023-10-27T10:00:00Z' },
      { id: 2, title: '云服务套餐报价', customer: { name: '李四' }, total_amount: 990.00, status: 'sent', created_at: '2023-10-28T11:00:00Z' },
    ];
  } catch (error) {
    console.error('Failed to fetch quotations:', error);
    ElMessage.error('获取报价单列表失败');
  }
};

const handleAdd = () => {
  ElMessage.info('前往新增报价单页面');
};

const handleEdit = (row) => {
  ElMessage.info(`编辑报价单: ${row.title}`);
};

const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm(`确定要删除报价单 "${row.title}" 吗？`, '警告', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    });
    // await apiClient.delete(`/quotations/${row.id}/`);
    quotations.value = quotations.value.filter(q => q.id !== row.id);
    ElMessage.success('删除成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败');
    }
  }
};
</script>

<style scoped>
.quotation-list {
  padding: 20px;
}
</style>