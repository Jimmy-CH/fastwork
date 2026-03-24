import axios from 'axios';

const apiClient = axios.create({
  baseURL: process.env.VUE_APP_API_BASE_URL || 'http://localhost:8000', // 后端API地址
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  }
});

// 请求拦截器
apiClient.interceptors.request.use(
  config => {
    // 从localStorage或store中获取token并添加到请求头
    const token = localStorage.getItem('authToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  error => Promise.reject(error)
);

// 响应拦截器
apiClient.interceptors.response.use(
  response => response.data,
  error => {
    console.error('API Error:', error);
    // 可以在这里统一处理错误，例如未登录跳转
    if (error.response?.status === 401) {
      // router.push('/login');
    }
    return Promise.reject(error);
  }
);

export default {
  // Accounts
  getRoles() {
    return apiClient.get('/accounts/roles/');
  },
  getDepartments() {
    return apiClient.get('/accounts/departments/');
  },
  getUsers(params) {
    return apiClient.get('/accounts/users/', params);
  },
  // Customer
  getCustomers(params) {
    return apiClient.get('/customer/customers/', params);
  },
  getQuotations(params) {
    return apiClient.get('/customer/quotations/', params);
  },
  // Product
  getProducts(params) {
    return apiClient.get('/product/products/', params);
  },
  getProductCategories(params) {
    return apiClient.get('/product/categories/', params);
  },
  // Warehouse
  getInventoryTransactions(params) {
    return apiClient.get('/warehouse/inventory_transactions/', params);
  },
  // KnowledgeBase
  getKnowledgeBaseArticles(params) {
    return apiClient.get('/knowledge_base/articles/', params);
  },
  getKnowledgeBaseCategories(params) {
    return apiClient.get('/knowledge_base/categories/', params);
  },
  // ... 其他模块的API方法
};