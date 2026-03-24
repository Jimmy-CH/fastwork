<template>
  <div class="config-list-container">
    <h2>系统配置</h2>
    
    <data-table
      :loading="loading"
      :table-data="configs"
      :columns="columns"
      :show-actions="true"
    >
      <template #actions="{ row }">
        <el-button size="small" @click="handleEdit(row)">编辑</el-button>
      </template>
    </data-table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { ElMessage } from 'element-plus'
import api from '@/api'
import DataTable from '@/components/Common/DataTable.vue'

const loading = ref(false)
const configs = ref([])

const columns = [
  { prop: 'id', label: 'ID', width: 100 },
  { prop: 'key', label: '配置键' },
  { prop: 'value', label: '值', width: 300 },
  { prop: 'description', label: '描述' },
  { prop: 'updated_at', label: '最后更新', formatter: (row, col, val) => new Date(val).toLocaleString() },
]

const fetchData = async () => {
  loading.value = true;
  try {
    // const response = await api.getConfigs();
    // 模拟数据
    configs.value = [
      { id: 1, key: 'site_name', value: '我的ERP系统', description: '系统显示的名称' },
      { id: 2, key: 'smtp_server', value: 'smtp.example.com', description: '邮件服务器地址' },
      { id: 3, key: 'default_language', value: 'zh-hans', description: '系统默认语言' },
    ];
  } catch (error) {
    console.error('获取系统配置列表失败:', error);
    ElMessage.error('获取列表失败');
  } finally {
    loading.value = false;
  }
};

const handleEdit = (row) => {
  ElMessage.info(`编辑配置项: ${row.key}`);
}

onMounted(() => {
  fetchData();
})
</script>