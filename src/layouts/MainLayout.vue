<script setup>
import { ref, computed } from 'vue'
import Sidebar from '../components/Sidebar.vue'
import Topbar from '../components/Topbar.vue'
import { useRoute } from 'vue-router'

const isHovering = ref(false)
const route = useRoute()

const showTopbar = computed(() => route.name !== 'profile') // Oculta el Topbar solo en la vista de perfil
</script>

<template>
    <div class="app-container" :class="{ collapsed: !isHovering }">

        <Sidebar @hover="isHovering = $event" />

        <main class="main-content">
            <Topbar v-if="showTopbar" />
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