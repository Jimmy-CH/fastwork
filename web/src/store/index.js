import { defineStore } from 'pinia'

export const useMainStore = defineStore('main', {
  state: () => ({
    sidebarCollapsed: false,
    currentUser: null,
    permissions: []
  }),
  actions: {
    toggleSidebar() {
      this.sidebarCollapsed = !this.sidebarCollapsed;
    },
    setCurrentUser(user) {
      this.currentUser = user;
    },
    setPermissions(permissions) {
      this.permissions = permissions;
    }
  }
})