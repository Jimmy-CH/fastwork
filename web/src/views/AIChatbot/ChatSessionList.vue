<!-- src/views/AIChatbot/ChatSessionList.vue -->
<template>
  <div class="chat-session-list">
    <h2>AI聊天记录</h2>
    <DataTable
      :data="sessions"
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

const sessions = ref([]);

const tableColumns = [
  { prop: 'id', label: 'ID' },
  { prop: 'session_id', label: '会话ID' },
  { prop: 'customer.name', label: '客户', formatter: (row) => row.customer?.name || '-' },
  { prop: 'created_at', label: '创建时间' },
];

onMounted(() => {
  loadSessions();
});

const loadSessions = async () => {
  try {
    // const response = await apiClient.get('/chat-sessions/');
    // sessions.value = response.data.results;
    // 模拟数据
    sessions.value = [
      { id: 1, session_id: 'sess_abc123', customer: { name: '李四' }, created_at: '2023-10-29T15:00:00Z' },
      { id: 2, session_id: 'sess_def456', customer: { name: '王五' }, created_at: '2023-10-30T16:00:00Z' },
    ];
  } catch (error) {
    console.error('Failed to fetch chat sessions:', error);
    ElMessage.error('获取AI聊天记录列表失败');
  }
};

const handleAdd = () => {
  ElMessage.info('前往新增聊天会话页面');
};

const handleEdit = (row) => {
  ElMessage.info(`编辑聊天会话: ${row.session_id}`);
};

const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm(`确定要删除聊天会话 "${row.session_id}" 吗？`, '警告', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    });
    // await apiClient.delete(`/chat-sessions/${row.id}/`);
    sessions.value = sessions.value.filter(s => s.id !== row.id);
    ElMessage.success('删除成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败');
    }
  }
};
</script>

<style scoped>
.chat-session-list {
  padding: 20px;
}
</style>