<!-- src/components/Layout/Header.vue -->
<template>
  <el-header class="header">
    <div class="left-section">
      <!-- 折叠按钮 -->
      <el-button icon="Fold" @click="toggleCollapse" size="large" text />
      <div class="header-title">{{ pageTitle }}</div>
    </div>

    <div class="user-info">
      <el-dropdown>
        <span class="el-dropdown-link">
          admin <el-icon class="el-icon--right"><arrow-down /></el-icon>
        </span>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item>个人中心</el-dropdown-item>
            <el-dropdown-item>退出登录</el-dropdown-item>
          </el-dropdown-menu>
          
        </template>
      </el-dropdown>
    </div>
  </el-header>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import { ArrowDown } from '@element-plus/icons-vue';

const route = useRoute();
const pageTitle = ref('');

const updateTitle = () => {
  const routeMap = {
    '/dashboard': '仪表盘',
    '/users': '用户管理',
    '/roles': '角色管理',
    '/departments': '部门管理',
    '/customers': '客户管理',
    '/quotations': '报价单管理',
    '/work-orders': '工单管理',
    '/feedbacks': '反馈管理',
    '/products': '产品管理',
    '/product-categories': '产品分类',
    '/bom': 'BOM清单',
    '/inventory': '库存管理',
    '/purchase-orders': '采购订单',
    '/inventory-transactions': '库存交易',
    '/mall-orders': '商城订单',
    '/chat-sessions': 'AI聊天记录',
    '/messages': '消息中心',
    '/articles': '知识库',
    '/kb-categories': '知识分类',
    '/configs': '系统配置',
  };
  pageTitle.value = routeMap[route.path] || 'FastWork';
};

updateTitle();
watch(() => route.path, updateTitle);
</script>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: white;
  box-shadow: 0 1px 4px rgba(0, 21, 41, 0.08);
  padding: 0 20px;
  line-height: 60px;
}
.header-title {
  font-size: 18px;
  font-weight: bold;
  color: var(--el-text-color-primary);
}
.user-info {
  cursor: pointer;
}
</style>