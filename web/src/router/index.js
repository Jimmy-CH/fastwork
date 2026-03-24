// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from '@/views/Dashboard.vue';

// Accounts
const UserList = () => import('@/views/Accounts/UserList.vue');
const RoleList = () => import('@/views/Accounts/RoleList.vue');
const DepartmentList = () => import('@/views/Accounts/DepartmentList.vue');

// Customer
const CustomerList = () => import('@/views/Customer/CustomerList.vue');
const QuotationList = () => import('@/views/Customer/QuotationList.vue');

// Service Order
const WorkOrderList = () => import('@/views/ServiceOrder/WorkOrderList.vue');
const FeedbackList = () => import('@/views/ServiceOrder/FeedbackList.vue');

// Product
const ProductList = () => import('@/views/Product/ProductList.vue');
const CategoryList = () => import('@/views/Product/CategoryList.vue');
const BOMList = () => import('@/views/Product/BOMList.vue');

// Warehouse
const PurchaseOrderList = () => import('@/views/Warehouse/PurchaseOrderList.vue');
const InventoryList = () => import('@/views/Warehouse/InventoryList.vue');
const InventoryTransactionList = () => import('@/views/Warehouse/InventoryTransactionList.vue');

// Mall
const MallOrderList = () => import('@/views/Mall/OrderList.vue');

// AI Chatbot
const ChatSessionList = () => import('@/views/AIChatbot/ChatSessionList.vue');

// Message Center
const MessageList = () => import('@/views/MessageCenter/MessageList.vue');

// Knowledge Base
const ArticleList = () => import('@/views/KnowledgeBase/ArticleList.vue');
const KBCategoryList = () => import('@/views/KnowledgeBase/CategoryList.vue');

// System Management
const ConfigList = () => import('@/views/SystemManagement/ConfigList.vue');

const routes = [
  { path: '/', redirect: '/dashboard' },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard },

  // Accounts Routes
  { path: '/users', name: 'UserList', component: UserList },
  { path: '/roles', name: 'RoleList', component: RoleList },
  { path: '/departments', name: 'DepartmentList', component: DepartmentList },

  // Customer Routes
  { path: '/customers', name: 'CustomerList', component: CustomerList },
  { path: '/quotations', name: 'QuotationList', component: QuotationList },

  // Service Order Routes
  { path: '/work-orders', name: 'WorkOrderList', component: WorkOrderList },
  { path: '/feedbacks', name: 'FeedbackList', component: FeedbackList },

  // Product Routes
  { path: '/products', name: 'ProductList', component: ProductList },
  { path: '/product-categories', name: 'ProductCategoryList', component: CategoryList },
  { path: '/bom', name: 'BOMList', component: BOMList },

  // Warehouse Routes
  { path: '/purchase-orders', name: 'PurchaseOrderList', component: PurchaseOrderList },
  { path: '/inventory', name: 'InventoryList', component: InventoryList },
  { path: '/inventory-transactions', name: 'InventoryTransactionList', component: InventoryTransactionList },

  // Mall Route
  { path: '/mall-orders', name: 'MallOrderList', component: MallOrderList },

  // AI Chatbot Route
  { path: '/chat-sessions', name: 'ChatSessionList', component: ChatSessionList },

  // Message Center Route
  { path: '/messages', name: 'MessageList', component: MessageList },

  // Knowledge Base Routes
  { path: '/articles', name: 'ArticleList', component: ArticleList },
  { path: '/kb-categories', name: 'KBCategoryList', component: KBCategoryList },

  // System Management Route
  { path: '/configs', name: 'ConfigList', component: ConfigList },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
