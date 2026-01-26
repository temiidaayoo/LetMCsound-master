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
    height: 100vh;
}


.app-container:not(.collapsed) .main-content {
    margin-left: 220px;
}

.main-content {
    flex: 1;
    transition: margin-left .3s ease;
    
}

html, body, .app-container {
    height: 100%;
}

</style>