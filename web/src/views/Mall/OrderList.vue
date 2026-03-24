<!-- src/views/Mall/OrderList.vue -->
<template>
  <div class="mall-order-list">
    <h2>商城订单</h2>
    <DataTable
      :data="orders"
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

const orders = ref([]);

const tableColumns = [
  { prop: 'id', label: 'ID' },
  { prop: 'order_number', label: '订单号' },
  { prop: 'customer.name', label: '客户', formatter: (row) => row.customer?.name || '-' },
  { prop: 'total_amount', label: '总金额', formatter: (row) => `¥${row.total_amount.toFixed(2)}` },
  { prop: 'status', label: '状态', formatter: (row) => ({'pending_payment': '待付款', 'paid': '已付款', 'shipped': '已发货', 'delivered': '已送达', 'cancelled': '已取消'})[row.status] || '未知' },
  { prop: 'shipping_address', label: '收货地址' },
  { prop: 'created_at', label: '创建时间' },
];

onMounted(() => {
  loadOrders();
});

const loadOrders = async () => {
  try {
    // const response = await apiClient.get('/mall-orders/');
    // orders.value = response.data.results;
    // 模拟数据
    orders.value = [
      { id: 1, order_number: 'ORD-001', customer: { name: '李四' }, total_amount: 199.00, status: 'paid', shipping_address: '北京市朝阳区xxx街道', created_at: '2023-10-29T10:00:00Z' },
      { id: 2, order_number: 'ORD-002', customer: { name: '王五' }, total_amount: 599.00, status: 'shipped', shipping_address: '上海市浦东新区xxx路', created_at: '2023-10-30T11:00:00Z' },
    ];
  } catch (error) {
    console.error('Failed to fetch orders:', error);
    ElMessage.error('获取商城订单列表失败');
  }
};

const handleAdd = () => {
  ElMessage.info('前往新增商城订单页面');
};

const handleEdit = (row) => {
  ElMessage.info(`编辑商城订单: ${row.order_number}`);
};

const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm(`确定要删除商城订单 "${row.order_number}" 吗？`, '警告', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    });
    // await apiClient.delete(`/mall-orders/${row.id}/`);
    orders.value = orders.value.filter(o => o.id !== row.id);
    ElMessage.success('删除成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败');
    }
  }
};
</script>

<style scoped>
.mall-order-list {
  padding: 20px;
}
</style>