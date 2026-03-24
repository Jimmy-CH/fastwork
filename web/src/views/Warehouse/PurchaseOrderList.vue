<!-- src/views/Warehouse/PurchaseOrderList.vue -->
<template>
  <div class="purchase-order-list">
    <h2>采购订单</h2>
    <DataTable
      :data="purchaseOrders"
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

const purchaseOrders = ref([]);

const tableColumns = [
  { prop: 'id', label: 'ID' },
  { prop: 'po_number', label: '订单号' },
  { prop: 'supplier', label: '供应商' },
  { prop: 'total_amount', label: '总金额', formatter: (row) => `¥${row.total_amount.toFixed(2)}` },
  { prop: 'status', label: '状态', formatter: (row) => ({'draft': '草稿', 'submitted': '已提交', 'approved': '已批准', 'received': '已收货', 'cancelled': '已取消'})[row.status] || '未知' },
  { prop: 'created_at', label: '创建时间' },
];

onMounted(() => {
  loadPurchaseOrders();
});

const loadPurchaseOrders = async () => {
  try {
    // const response = await apiClient.get('/purchase-orders/');
    // purchaseOrders.value = response.data.results;
    // 模拟数据
    purchaseOrders.value = [
      { id: 1, po_number: 'PO-001', supplier: 'ABC供应商', total_amount: 50000.00, status: 'approved', created_at: '2023-10-25T09:00:00Z' },
      { id: 2, po_number: 'PO-002', supplier: 'XYZ供应商', total_amount: 12000.00, status: 'submitted', created_at: '2023-10-26T10:00:00Z' },
    ];
  } catch (error) {
    console.error('Failed to fetch purchase orders:', error);
    ElMessage.error('获取采购订单列表失败');
  }
};

const handleAdd = () => {
  ElMessage.info('前往新增采购订单页面');
};

const handleEdit = (row) => {
  ElMessage.info(`编辑采购订单: ${row.po_number}`);
};

const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm(`确定要删除采购订单 "${row.po_number}" 吗？`, '警告', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    });
    // await apiClient.delete(`/purchase-orders/${row.id}/`);
    purchaseOrders.value = purchaseOrders.value.filter(po => po.id !== row.id);
    ElMessage.success('删除成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败');
    }
  }
};
</script>

<style scoped>
.purchase-order-list {
  padding: 20px;
}
</style>