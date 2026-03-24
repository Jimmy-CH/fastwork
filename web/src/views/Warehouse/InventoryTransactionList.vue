<!-- src/views/Warehouse/InventoryTransactionList.vue -->
<template>
  <div class="transaction-list">
    <h2>库存交易流水</h2>
    <DataTable
      :data="transactions"
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

const transactions = ref([]);

const tableColumns = [
  { prop: 'id', label: 'ID' },
  { prop: 'product.name', label: '产品', formatter: (row) => row.product?.name || '-' },
  { prop: 'transaction_type', label: '类型', formatter: (row) => ({'in': '入库', 'out': '出库'})[row.transaction_type] || '未知' },
  { prop: 'quantity', label: '数量' },
  { prop: 'reference_doc', label: '参考单据' },
  { prop: 'notes', label: '备注' },
  { prop: 'timestamp', label: '时间戳' },
];

onMounted(() => {
  loadTransactions();
});

const loadTransactions = async () => {
  try {
    // const response = await apiClient.get('/inventory-transactions/');
    // transactions.value = response.data.results;
    // 模拟数据
    transactions.value = [
      { id: 1, product: { name: '高性能服务器' }, transaction_type: 'in', quantity: 10, reference_doc: 'PO-001', notes: '采购入库', timestamp: '2023-10-27T14:00:00Z' },
      { id: 2, product: { name: '高性能服务器' }, transaction_type: 'out', quantity: 2, reference_doc: 'WO-001', notes: '工单领料', timestamp: '2023-10-28T15:00:00Z' },
    ];
  } catch (error) {
    console.error('Failed to fetch transactions:', error);
    ElMessage.error('获取库存交易列表失败');
  }
};

const handleAdd = () => {
  ElMessage.info('前往新增库存交易页面');
};

const handleEdit = (row) => {
  ElMessage.info(`编辑交易 ID: ${row.id}`);
};

const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm(`确定要删除交易记录吗？`, '警告', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    });
    // await apiClient.delete(`/inventory-transactions/${row.id}/`);
    transactions.value = transactions.value.filter(t => t.id !== row.id);
    ElMessage.success('删除成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败');
    }
  }
};
</script>

<style scoped>
.transaction-list {
  padding: 20px;
}
</style>