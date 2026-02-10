<script>
import { useTheme } from '../composables/useTheme'

export default {
    name: "ConfigView",
    setup() {
        const { theme, applyTheme } = useTheme()
        return { theme, applyTheme }
    },
    data() {
        return {
            // Profile data
            name: 'Usuario',
            email: 'usuario@email.com',
            profilePhoto: '/assets/letmc.png',
            
            // Password change
            currentPassword: '',
            newPassword: '',
            confirmPassword: '',
            
            // 2FA
            twoFactorEnabled: false,
            
            // Personal info
            phone: '',
            bio: '',
            location: '',
            
            // Preferences
            language: 'es',
            timezone: 'Europe/Madrid',
            
            languages: [
                { value: 'es', label: 'Español' },
                { value: 'en', label: 'English' },
                { value: 'fr', label: 'Français' },
                { value: 'de', label: 'Deutsch' }
            ],
            
            timezones: [
                { value: 'Europe/Madrid', label: 'Europa/Madrid (UTC+1)' },
                { value: 'Europe/London', label: 'Europa/London (UTC+0)' },
                { value: 'America/New_York', label: 'America/New_York (UTC-5)' },
                { value: 'America/Los_Angeles', label: 'America/Los_Angeles (UTC-8)' },
                { value: 'Asia/Tokyo', label: 'Asia/Tokyo (UTC+9)' }
            ],
            
            themes: [
                { value: 'dark', label: 'Oscuro' },
                { value: 'light', label: 'Claro' }
            ]
        }
    },
    watch: {
        theme(newTheme) {
            this.applyTheme(newTheme)
        }
    },
    mounted() {
        // El tema ya se carga desde useTheme composable
    },
    methods: {
        saveProfile() {
            console.log('Guardando perfil:', this.name, this.email)
            alert('Perfil guardado correctamente')
        },
        changePassword() {
            if (this.newPassword !== this.confirmPassword) {
                alert('Las contraseñas no coinciden')
                return
            }
            console.log('Cambiando contraseña')
            alert('Contraseña actualizada correctamente')
            this.currentPassword = ''
            this.newPassword = ''
            this.confirmPassword = ''
        },
        toggleTwoFactor() {
            console.log('2FA:', this.twoFactorEnabled ? 'Activado' : 'Desactivado')
            alert(this.twoFactorEnabled ? 'Verificación en dos pasos activada' : 'Verificación en dos pasos desactivada')
        },
        savePreferences() {
            console.log('Guardando preferencias:', this.language, this.timezone, this.theme)
            alert('Preferencias guardadas correctamente')
        },
        handlePhotoUpload(event) {
            const file = event.target.files[0]
            if (file) {
                this.profilePhoto = URL.createObjectURL(file)
                alert('Foto de perfil actualizada')
            }
        }
    }
}
</script>

<template>
    <div class="config-page">
        <h1>Configuration</h1>
        
        <!-- Perfil -->
        <section class="config-section">
            <h2><i class="ri-user-3-fill"></i> Perfil</h2>
            
            <div class="form-group">
                <label>Nombre</label>
                <input type="text" v-model="name" placeholder="Tu nombre">
            </div>
            
            <div class="form-group">
                <label>Correo electrónico</label>
                <input type="email" v-model="email" placeholder="tu@email.com">
            </div>
            
            <button class="btn-primary" @click="saveProfile">Guardar perfil</button>
        </section>

        <!-- Cambio de contraseña -->
        <section class="config-section">
            <h2><i class="ri-lock-fill"></i> Cambio de contraseña</h2>
            
            <div class="form-group">
                <label>Contraseña actual</label>
                <input type="password" v-model="currentPassword" placeholder="••••••••">
            </div>
            
            <div class="form-group">
                <label>Nueva contraseña</label>
                <input type="password" v-model="newPassword" placeholder="••••••••">
            </div>
            
            <div class="form-group">
                <label>Confirmar contraseña</label>
                <input type="password" v-model="confirmPassword" placeholder="••••••••">
            </div>
            
            <button class="btn-primary" @click="changePassword">Cambiar contraseña</button>
        </section>

        <!-- Verificación en dos pasos -->
        <section class="config-section">
            <h2><i class="ri-shield-check-fill"></i> Verificación en dos pasos</h2>
            
            <div class="toggle-group">
                <div class="toggle-info">
                    <span class="toggle-label">Activar 2FA</span>
                    <span class="toggle-desc">Añade una capa extra de seguridad a tu cuenta</span>
                </div>
                <label class="switch">
                    <input type="checkbox" v-model="twoFactorEnabled" @change="toggleTwoFactor">
                    <span class="slider"></span>
                </label>
            </div>
        </section>

        <!-- Información personal -->
        <section class="config-section">
            <h2><i class="ri-edit-box-fill"></i> Información personal</h2>
            
            <div class="form-group">
                <label>Teléfono</label>
                <input type="tel" v-model="phone" placeholder="+34 600 000 000">
            </div>
            
            <div class="form-group">
                <label>Biografía</label>
                <textarea v-model="bio" placeholder="Cuéntanos sobre ti..." rows="3"></textarea>
            </div>
            
            <div class="form-group">
                <label>Ubicación</label>
                <input type="text" v-model="location" placeholder="Ciudad, País">
            </div>
            
            <button class="btn-primary" @click="saveProfile">Guardar información</button>
        </section>

        <!-- Preferencias -->
        <section class="config-section">
            <h2><i class="ri-settings-3-fill"></i> Preferencias</h2>
            
            <div class="form-group">
                <label>Idioma</label>
                <select v-model="language">
                    <option v-for="lang in languages" :key="lang.value" :value="lang.value">
                        {{ lang.label }}
                    </option>
                </select>
            </div>
            
            <div class="form-group">
                <label>Zona horaria</label>
                <select v-model="timezone">
                    <option v-for="tz in timezones" :key="tz.value" :value="tz.value">
                        {{ tz.label }}
                    </option>
                </select>
            </div>
            
            <div class="form-group">
                <label>Tema</label>
                <div class="theme-selector">
                    <label v-for="t in themes" :key="t.value" 
                           class="theme-option" 
                           :class="{ active: theme === t.value }">
                        <input type="radio" :value="t.value" v-model="theme" hidden>
                        <i :class="t.value === 'dark' ? 'ri-moon-fill' : 'ri-sun-fill'"></i>
                        <span>{{ t.label }}</span>
                    </label>
                </div>
            </div>
            
            <button class="btn-primary" @click="savePreferences">Guardar preferencias</button>
        </section>
    </div>
</template>

<style scoped>
.config-page {
    padding: 2rem;
    max-width: 100%;
    margin: 0 auto;
}

.config-section {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.1);
}

.config-section h2 {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
    font-size: 1.25rem;
    color: #fff;
}

.config-section h2 i {
    color: #b11db9;
}


.form-group {
    margin-bottom: 1rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    color: #aaa;
    font-size: 0.875rem;
}

.form-group input,
.form-group select,
.form-group textarea {
    width: 100%;
    padding: 0.75rem;
    background: rgba(0, 0, 0, 0.3);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    color: #fff;
    font-size: 1rem;
    transition: border-color 0.2s;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    outline: none;
    border-color: #b11db9;
}

.form-group textarea {
    resize: vertical;
}

.btn-primary {
    background: #b11db9;
    color: #fff;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1rem;
    transition: background 0.2s, transform 0.2s;
}

.btn-primary:hover {
    background: #9a18a3;
    transform: translateY(-2px);
}

.toggle-group {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    background: rgba(0, 0, 0, 0.2);
    border-radius: 8px;
}

.toggle-label {
    display: block;
    color: #fff;
    font-weight: 500;
}

.toggle-desc {
    display: block;
    color: #888;
    font-size: 0.875rem;
    margin-top: 0.25rem;
}

.switch {
    position: relative;
    display: inline-block;
    width: 50px;
    height: 26px;
}

.switch input {
    opacity: 0;
    width: 0;
    height: 0;
}

.slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #333;
    transition: 0.3s;
    border-radius: 26px;
}

.slider:before {
    position: absolute;
    content: "";
    height: 20px;
    width: 20px;
    left: 3px;
    bottom: 3px;
    background-color: white;
    transition: 0.3s;
    border-radius: 50%;
}

input:checked + .slider {
    background-color: #b11db9;
}

input:checked + .slider:before {
    transform: translateX(24px);
}

.theme-selector {
    display: flex;
    gap: 1rem;
}

.theme-option {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
    padding: 1rem;
    background: rgba(0, 0, 0, 0.2);
    border: 2px solid transparent;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.2s;
}

.theme-option.active {
    border-color: #b11db9;
    background: rgba(177, 29, 185, 0.1);
}

.theme-option i {
    font-size: 1.5rem;
    color: #fff;
}

.theme-option span {
    color: #aaa;
    font-size: 0.875rem;
}
</style>
