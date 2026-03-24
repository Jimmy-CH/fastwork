<!-- src/components/Layout/Sidebar.vue -->
<template>
  <div class="sidebar">
    <h3 v-show="!isCollapse">FastWork</h3>
    <h3 v-show="isCollapse" class="logo-mini">F</h3>
    <!-- 添加 collapse 属性到 el-menu -->
    <el-menu
      :default-active="$route.path"
      class="el-menu-vertical"
      router
      unique-opened
      :collapse="isCollapse"
      :collapse-transition="false" 
    >
      <el-menu-item index="/dashboard">
        <el-icon><House /></el-icon>
        <span>仪表盘</span>
      </el-menu-item>

      <el-sub-menu index="account">
        <template #title>
          <el-icon><User /></el-icon>
          <span>账号管理</span>
        </template>
        <el-menu-item index="/users">用户</el-menu-item>
        <el-menu-item index="/roles">角色</el-menu-item>
        <el-menu-item index="/departments">部门</el-menu-item>
      </el-sub-menu>

      <el-sub-menu index="customer">
        <template #title>
          <el-icon><OfficeBuilding /></el-icon>
          <span>客户管理</span>
        </template>
        <el-menu-item index="/customers">客户</el-menu-item>
        <el-menu-item index="/quotations">报价单</el-menu-item>
      </el-sub-menu>

      <el-sub-menu index="service">
        <template #title>
          <el-icon><Service /></el-icon>
          <span>工单服务</span>
        </template>
        <el-menu-item index="/work-orders">工单</el-menu-item>
        <el-menu-item index="/feedbacks">反馈</el-menu-item>
      </el-sub-menu>

      <el-sub-menu index="product">
        <template #title>
          <el-icon><ShoppingBag /></el-icon>
          <span>产品管理</span>
        </template>
        <el-menu-item index="/products">产品</el-menu-item>
        <el-menu-item index="/product-categories">产品分类</el-menu-item>
        <el-menu-item index="/bom">BOM清单</el-menu-item>
      </el-sub-menu>

      <el-sub-menu index="warehouse">
        <template #title>
          <el-icon><Box /></el-icon>
          <span>仓储管理</span>
        </template>
        <el-menu-item index="/inventory">库存</el-menu-item>
        <el-menu-item index="/purchase-orders">采购单</el-menu-item>
        <el-menu-item index="/inventory-transactions">库存流水</el-menu-item>
      </el-sub-menu>

      <el-sub-menu index="mall">
        <template #title>
          <el-icon><ShoppingCart /></el-icon>
          <span>商城</span>
        </template>
        <el-menu-item index="/mall-orders">订单</el-menu-item>
      </el-sub-menu>

      <el-sub-menu index="ai_kb">
        <template #title>
          <el-icon><ChatLineRound /></el-icon>
          <span>AI与知识</span>
        </template>
        <el-menu-item index="/chat-sessions">AI对话</el-menu-item>
        <el-menu-item index="/articles">知识库</el-menu-item>
        <el-menu-item index="/kb-categories">知识分类</el-menu-item>
      </el-sub-menu>

      <el-sub-menu index="system">
        <template #title>
          <el-icon><Setting /></el-icon>
          <span>系统</span>
        </template>
        <el-menu-item index="/messages">消息中心</el-menu-item>
        <el-menu-item index="/configs">系统配置</el-menu-item>
      </el-sub-menu>
    </el-menu>
  </div>
</template>

<script setup>
import { House, User, OfficeBuilding, Service, ShoppingBag, Box, ShoppingCart, ChatLineRound, Setting } from '@element-plus/icons-vue';

// 接收父组件传来的折叠状态
defineProps({
  isCollapse: {
    type: Boolean,
    required: true,
  }
});
</script>

<style scoped>
.sidebar {
  height: 100%;
  padding-top: 20px;
  box-shadow: 2px 0 6px rgba(0, 21, 41, 0.35);
  z-index: 100;
}

.sidebar h3 {
  color: var(--el-text-color-primary);
  text-align: center;
  margin-bottom: 20px;
  transition: all 0.3s;
}

.logo-mini {
  font-size: 24px;
  margin-bottom: 20px;
}

.el-menu {
  border-right: none;
  --el-menu-bg-color: transparent;
  --el-menu-base-level-padding: 0;
  --el-menu-item-height: 50px;
}

.el-menu--collapse .el-menu-item span,
.el-menu--collapse .el-sub-menu__title span {
  display: none;
}

.el-menu--collapse .el-menu-item,
.el-menu--collapse .el-sub-menu__title {
  justify-content: center;
}
</style>