<!-- src/views/MessageCenter/MessageList.vue -->
<template>
  <div class="message-list">
    <h2>消息中心</h2>
    <DataTable
      :data="messages"
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

const messages = ref([]);

const tableColumns = [
  { prop: 'id', label: 'ID' },
  { prop: 'title', label: '标题' },
  { prop: 'content', label: '内容' },
  { prop: 'recipient_user.user.first_name', label: '接收者', formatter: (row) => row.recipient_user?.user?.first_name || '-' },
  { prop: 'message_type', label: '类型', formatter: (row) => ({'notification': '通知', 'alert': '警报', 'reminder': '提醒'})[row.message_type] || '未知' },
  { prop: 'is_read', label: '已读', formatter: (row) => row.is_read ? '是' : '否' },
  { prop: 'created_at', label: '创建时间' },
];

onMounted(() => {
  loadMessages();
});

const loadMessages = async () => {
  try {
    // const response = await apiClient.get('/messages/');
    // messages.value = response.data.results;
    // 模拟数据
    messages.value = [
      { id: 1, title: '新工单指派', content: '您有一个新的高优先级工单需要处理。', recipient_user: { user: { first_name: '张' }}, message_type: 'alert', is_read: false, created_at: '2023-10-30T17:00:00Z' },
      { id: 2, title: '系统维护通知', content: '系统将于明晚进行维护，请提前做好准备。', recipient_user: { user: { first_name: '李' }}, message_type: 'notification', is_read: true, created_at: '2023-10-29T18:00:00Z' },
    ];
  } catch (error) {
    console.error('Failed to fetch messages:', error);
    ElMessage.error('获取消息列表失败');
  }
};

const handleAdd = () => {
  ElMessage.info('前往新增消息页面');
};

const handleEdit = (row) => {
  ElMessage.info(`编辑消息: ${row.title}`);
};

const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm(`确定要删除消息 "${row.title}" 吗？`, '警告', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    });
    // await apiClient.delete(`/messages/${row.id}/`);
    messages.value = messages.value.filter(m => m.id !== row.id);
    ElMessage.success('删除成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败');
    }
  }
};
</script>

<style scoped>
.message-list {
  padding: 20px;
}
</style>