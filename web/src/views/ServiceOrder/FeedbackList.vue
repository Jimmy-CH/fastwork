<!-- src/views/ServiceOrder/FeedbackList.vue -->
<template>
  <div class="feedback-list">
    <h2>反馈管理</h2>
    <DataTable
      :data="feedbacks"
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

const feedbacks = ref([]);

const tableColumns = [
  { prop: 'id', label: 'ID' },
  { prop: 'work_order.title', label: '关联工单', formatter: (row) => row.work_order?.title || '-' },
  { prop: 'satisfaction_rating', label: '满意度' },
  { prop: 'comments', label: '评论' },
  { prop: 'created_at', label: '创建时间' },
];

onMounted(() => {
  loadFeedbacks();
});

const loadFeedbacks = async () => {
  try {
    // const response = await apiClient.get('/feedbacks/');
    // feedbacks.value = response.data.results;
    // 模拟数据
    feedbacks.value = [
      { id: 1, work_order: { title: '服务器宕机' }, satisfaction_rating: 5, comments: '问题解决迅速，服务很好！', created_at: '2023-10-29T15:00:00Z' },
      { id: 2, work_order: { title: '新功能咨询' }, satisfaction_rating: 4, comments: '解答详细，但等待时间稍长。', created_at: '2023-10-30T16:00:00Z' },
    ];
  } catch (error) {
    console.error('Failed to fetch feedbacks:', error);
    ElMessage.error('获取反馈列表失败');
  }
};

const handleAdd = () => {
  ElMessage.info('前往新增反馈页面');
};

const handleEdit = (row) => {
  ElMessage.info(`编辑反馈 ID: ${row.id}`);
};

const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm(`确定要删除反馈吗？`, '警告', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    });
    // await apiClient.delete(`/feedbacks/${row.id}/`);
    feedbacks.value = feedbacks.value.filter(f => f.id !== row.id);
    ElMessage.success('删除成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败');
    }
  }
};
</script>

<style scoped>
.feedback-list {
  padding: 20px;
}
</style>