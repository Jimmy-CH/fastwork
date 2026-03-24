<template>
  <div class="kb-category-list-container">
    <h2>知识库分类</h2>
    <el-button type="primary" @click="handleCreate" style="margin-bottom: 20px;">新增分类</el-button>
    
    <data-table
      :loading="loading"
      :table-data="categories"
      :columns="columns"
      :show-actions="true"
    >
      <template #actions="{ row }">
        <el-button size="small" @click="handleEdit(row)">编辑</el-button>
        <el-button size="small" type="danger" @click="handleDelete(row)">删除</el-button>
      </template>
    </data-table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import api from '@/api'
import DataTable from '@/components/Common/DataTable.vue'

const loading = ref(false)
const categories = ref([])

const columns = [
  { prop: 'id', label: 'ID', width: 100 },
  { prop: 'name', label: '名称' },
  { prop: 'description', label: '描述' },
  { prop: 'article_count', label: '文章数', width: 100 },
  { prop: 'created_at', label: '创建时间', formatter: (row, col, val) => new Date(val).toLocaleString() },
]

const fetchData = async () => {
  loading.value = true;
  try {
    // const response = await api.getKnowledgeBaseCategories();
    // 模拟数据
    categories.value = [
      { id: 1, name: '操作指南', description: '各类操作手册和教程', article_count: 15 },
      { id: 2, name: '故障排查', description: '常见问题及解决方案', article_count: 8 },
      { id: 3, name: '最佳实践', description: '推荐的工作流程和方法', article_count: 5 },
    ];
  } catch (error) {
    console.error('获取知识库分类列表失败:', error);
    ElMessage.error('获取列表失败');
  } finally {
    loading.value = false;
  }
};

const handleCreate = () => {
  ElMessage.info('跳转到新建分类页面');
}

const handleEdit = (row) => {
  ElMessage.info(`编辑分类: ${row.name}`);
}

const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm(`确定要删除分类 "${row.name}" 吗？`, '确认删除', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    });
    // await api.deleteKnowledgeBaseCategory(row.id);
    ElMessage.success('删除成功');
    fetchData();
  } catch {
    // 用户取消
  }
}

onMounted(() => {
  fetchData();
})
</script>