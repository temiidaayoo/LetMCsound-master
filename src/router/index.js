import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProfileView from '../views/ProfileView.vue'
import SoundView from '../views/SoundView.vue'
import MusiciansView from '../views/MusiciansView.vue'
import LyricsView from '../views/LyricsView.vue'
import ConfigView from '@/views/ConfigView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/profile',
            name: 'profile',
            component: ProfileView
        },
        {
            path: '/sound',
            name: 'sound',
            component: SoundView
        },
        {
            path: '/musicians',
            name: 'musicians',
            component: MusiciansView
        },
        {
            path: '/lyrics',
            name: 'lyrics',
            component: LyricsView
        },
        {
            path: '/configuration',
            name: 'configuration',
            component: ConfigView
        }
    ]
})

export default router 