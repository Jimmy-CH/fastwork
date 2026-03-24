<!-- src/views/KnowledgeBase/ArticleList.vue -->
<template>
  <div class="article-list">
    <h2>知识库</h2>
    <DataTable
      :data="articles"
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

const articles = ref([]);

const tableColumns = [
  { prop: 'id', label: 'ID' },
  { prop: 'title', label: '标题' },
  { prop: 'author', label: '作者' },
  { prop: 'category.name', label: '分类', formatter: (row) => row.category?.name || '-' },
  { prop: 'tags', label: '标签' },
  { prop: 'is_published', label: '发布', formatter: (row) => row.is_published ? '是' : '否' },
  { prop: 'created_at', label: '创建时间' },
];

onMounted(() => {
  loadArticles();
});

const loadArticles = async () => {
  try {
    // const response = await apiClient.get('/kb-articles/');
    // articles.value = response.data.results;
    // 模拟数据
    articles.value = [
      { id: 1, title: '如何创建工单', author: '张三', category: { name: '操作指南' }, tags: '工单,创建', is_published: true, created_at: '2023-10-28T09:00:00Z' },
      { id: 2, title: '产品A常见问题', author: '李四', category: { name: '常见问题' }, tags: '产品A,FAQ', is_published: true, created_at: '2023-10-29T10:00:00Z' },
    ];
  } catch (error) {
    console.error('Failed to fetch articles:', error);
    ElMessage.error('获取知识库文章列表失败');
  }
};

const handleAdd = () => {
  ElMessage.info('前往新增知识库文章页面');
};

const handleEdit = (row) => {
  ElMessage.info(`编辑文章: ${row.title}`);
};

const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm(`确定要删除文章 "${row.title}" 吗？`, '警告', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    });
    // await apiClient.delete(`/kb-articles/${row.id}/`);
    articles.value = articles.value.filter(a => a.id !== row.id);
    ElMessage.success('删除成功');
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败');
    }
  }
};
</script>

<style scoped>
.article-list {
  padding: 20px;
}
</style>