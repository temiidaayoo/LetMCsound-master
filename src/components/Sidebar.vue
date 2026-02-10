<script setup>
import { useTheme } from '../composables/useTheme'

const { theme, toggleTheme } = useTheme()
</script>

<template>
    <aside class="sidebar"
        @mouseenter="$emit('hover', true)"
        @mouseleave="$emit('hover', false)">
        <div class="logo-container">
            <img src="/assets/letmc.png" alt="Logo LETMC" class="logo-img">
        </div>
    
    <nav class="menu">
        
        <router-link to="/" active-class="active"> 
            <i class="ri-home-smile-2-fill"></i> <span>Home</span>
        </router-link>
        
        <router-link to="/profile" active-class="active"> 
            <i class="ri-user-3-fill"></i> <span>Profile</span>
        </router-link>
        
        <router-link to="/sound" active-class="active"> 
            <i class="ri-music-2-fill"></i> <span>Sounds</span>
        </router-link>

        <router-link to="/lyrics" active-class="active"> 
            <i class="ri-folder-music-fill"></i> <span>Lyrics</span>
        </router-link>

        <a href="#"> <i class="ri-brush-fill"></i> <span>Graphic Design</span></a>
        <a href="#"> <i class="ri-clapperboard-fill"></i> <span>Film Makers</span></a>
        
        <router-link to="/musicians" active-class="active"> 
            <i class="ri-disc-fill"></i> <span>Musicians</span>
        </router-link>

        <router-link to="/configuration" active-class="active"> 
            <i class="ri-settings-3-fill"></i> <span>Configuration</span>
        </router-link>
        </nav>

    </aside>
</template>

<style scoped>
.sidebar {
  position: fixed;        /* 🔥 sidebar fijo */
  top: 0;
  left: 0;
  width: 70px;            /* colapsado */
  height: 100vh;          /* ocupa toda la pantalla */
  overflow-y: auto;
  overflow-x: hidden;
  transition: width .3s ease;
}

.sidebar:hover {
    width: 220px;
}

/* Ocultar texto cuando está colapsado */
.sidebar .menu span {
    opacity: 0;
    white-space: nowrap;
    transition: opacity 0.2s ease;

}

/* Mostrar texto cuando se expande */
.sidebar:hover .menu span {
    opacity: 1;
}

        /* Alinear iconos y texto */
.menu a,
.menu router-link {
    display: flex;
    align-items: center;
    padding: 12px;
    gap: 10px;
}

        /* Ajustar iconos */
.menu i {
    font-size: 22px;
}

/* Theme Toggle Button */
.theme-toggle-btn {
    all: unset;
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 12px;
    cursor: pointer;
    color: var(--text-muted, #ccc);
    transition: all 0.2s;
    margin-top: auto;
    border-top: 1px solid var(--border-color, #333);
}

.theme-toggle-btn:hover {
    color: var(--text-primary, #fff);
    background: var(--bg-secondary, rgba(255, 255, 255, 0.05));
}

.theme-toggle-btn i {
    font-size: 22px;
}

.theme-toggle-btn span {
    opacity: 0;
    white-space: nowrap;
    transition: opacity 0.2s ease;
}

.sidebar:hover .theme-toggle-btn span {
    opacity: 1;
}
</style>

