<script setup>
import { ref } from 'vue'
import Sidebar from '../components/Sidebar.vue'
import Topbar from '../components/Topbar.vue'

const isHovering = ref(false)
</script>

<template>
    <div class="app-container" :class="{ collapsed: !isHovering }">

        <Sidebar @hover="isHovering = $event" />

        <main class="main-content">
            <Topbar />
            <router-view />
        </main>
    </div>
</template>

<style scoped>  
.app-container {
  display: flex;
}

.app-container.collapsed .main-content {
  margin-left: 70px;      /* ancho del sidebar colapsado */
}

.app-container:not(.collapsed) .main-content {
  margin-left: 220px;     /* ancho del sidebar expandido */
}

.main-content {
  width: 100%;
  overflow-y: auto;       /* 🔥 el scroll ocurre aquí */
  height: 100vh;          /* ocupa toda la pantalla */
  transition: margin-left .3s ease;
}

</style>