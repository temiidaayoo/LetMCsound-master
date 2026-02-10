<template>
  <div>
    <div v-if="!isAuthenticated" class="auth-container">
      <div class="auth-box">
        
        <div class="auth-header-nav">
            <a href="/" class="home-btn" title="Volver a Inicio">
                <i class="ri-home-4-fill"></i> Home
            </a>
        </div>

        <h2 class="auth-title">{{ showRegister ? 'Crear Cuenta' : 'Bienvenido' }}</h2>
        
        <form @submit.prevent="handleSubmit" class="auth-form">
          <div class="input-group">
            <label>Usuario</label>
            <input type="text" v-model="form.username" required placeholder="Tu usuario">
          </div>
          
          <div class="input-group">
            <label>Contraseña</label>
            <input type="password" v-model="form.password" required placeholder="Tu contraseña">
            <p v-if="showRegister" class="password-hint">
              Mínimo 8 caracteres, 1 Mayúscula, 1 Número, 1 Símbolo
            </p>
          </div>

          <button type="submit" class="auth-btn">
            {{ showRegister ? 'Registrarse' : 'Entrar' }}
          </button>
        </form>

        <p class="error-msg" v-if="errorMessage">{{ errorMessage }}</p>

        <div class="toggle-auth">
          <p>
            {{ showRegister ? '¿Ya tienes cuenta?' : '¿Nuevo en KairoWave?' }}
            <span @click="toggleMode">{{ showRegister ? 'Inicia Sesión' : 'Regístrate' }}</span>
          </p>
        </div>
      </div>
    </div>

    <div v-else class="profile-content animate-fade-in">

        <section class="profile-header-modern">
          <div class="header-content">
            <div class="text-info">
              <h1 class="artist-name">KAIRO WAVE</h1>
              <p class="artist-bio">
                "I specialize in Brazilian funk and Jersey. I love working with fast rhythms..."
              </p>
            </div>
          </div>
          <div class="profile-pic-container">
            <img src="/assets/kairowaveprofile.PNG" alt="Kairo Wave" class="profile-img">
          </div>
        </section>

        <section class="section">
          <div class="section-header">
            <h2>PROJECTS</h2>
            <i class="ri-more-fill"></i>
          </div>
          
          <div class="project-grid">
            <div class="project-card" @click="abrirModalBeat" style="background-image: url('/assets/kairoportada1.jpg');">
              <div class="project-info">
                 <h3>Beat Funk MC Santana x MC Dayo</h3>
                 <p>Genre: Brazilian Funk - 140 BPM</p>
                  <div class="project-stats">
                     <span>Beat</span>
                     <span><i class="ri-heart-fill"></i> 2.3k</span>
                 </div>
             </div>
           </div>
           
           <div class="project-card" style="background-image: url('/assets/kairoportada2 .jpg');">
              <div class="project-info">
                 <h3>Top Tier - KairoWave</h3>
                 <p>Genre: Jersey, Drill</p>
                  <div class="project-stats"><span>Song</span><span><i class="ri-heart-fill"></i> 1.9k</span></div>
             </div>
           </div>

            <div class="project-card" style="background-image: url('/assets/kairoportada3.jpg');">
              <div class="project-info">
                 <h3>Beat SexyDrill "YodaYd"</h3>
                 <p>Genre: Jersey, Drill</p>
                  <div class="project-stats"><span>Beat</span><span><i class="ri-heart-fill"></i> 1.9k</span></div>
             </div>
           </div>

            <div class="project-card" style="background-image: url('/assets/kairoportada4.jpg');">
              <div class="project-info">
                 <h3>Obsessed - KairoWave</h3>
                 <p>Genre: R&B</p>
                  <div class="project-stats"><span>Song</span><span><i class="ri-heart-fill"></i> 1.9k</span></div>
             </div>
           </div>
          </div>
        </section>

        <section class="section">
           <div class="section-header">
              <h2>POPULAR</h2>
              <i class="ri-more-fill"></i>
          </div>
          <div class="project-grid">
             <div class="project-card" style="background-image: url('/assets/kairoportada4.jpg');">
                <div class="project-info">
                   <h3>Obsessed - KairoWave</h3>
                   <p>Genre: R&B</p>
                    <div class="project-stats"><span>Song</span><span><i class="ri-heart-fill"></i> 5.9k</span></div>
               </div>
             </div>
              <div class="project-card" style="background-image: url('/assets/kairoportada1.jpg');">
                <div class="project-info">
                   <h3>Beat Funk MC Santana</h3>
                   <p>Genre: Brazilian Funk</p>
                    <div class="project-stats"><span>Beat</span><span><i class="ri-heart-fill"></i> 3.1k</span></div>
               </div>
             </div>
              <div class="project-card" style="background-image: url('/assets/kairoportada2 .jpg');">
                <div class="project-info">
                   <h3>Top Tier - KairoWave</h3>
                   <p>Genre: Jersey</p>
                    <div class="project-stats"><span>Song</span><span><i class="ri-heart-fill"></i> 2.8k</span></div>
               </div>
             </div>
              <div class="project-card" style="background-image: url('/assets/kairoportada3.jpg');">
                <div class="project-info">
                   <h3>Beat SexyDrill</h3>
                   <p>Genre: Jersey, Drill</p>
                    <div class="project-stats"><span>Beat</span><span><i class="ri-heart-fill"></i> 1.5k</span></div>
               </div>
             </div>
          </div>
        </section>
    </div>

    <div v-if="mostrarModal" class="modal-overlay" @click.self="cerrarModal">
        <div class="modal-content">
            <button class="close-modal" @click="cerrarModal">&times;</button>
            
            <div class="modal-grid">
                <div class="modal-left">
                    <img src="/assets/kairoportada1.jpg" alt="Portada" class="modal-img">
                    
                    <div class="audio-player-container">
                        <p class="audio-label">Preview Track</p>
                        <audio controls class="custom-audio">
                            <source :src="audioSource" type="audio/mpeg">
                            Tu navegador no soporta audio.
                        </audio>
                    </div>

                    <div class="beat-details">
                        <h4>Detalles Técnicos</h4>
                        <ul>
                            <li><strong>BPM:</strong> 140</li>
                            <li><strong>Key:</strong> A Minor</li>
                            <li><strong>Scale:</strong> Phrygian</li>
                            <li><strong>Date:</strong> Jan 2026</li>
                        </ul>
                    </div>
                </div>

                <div class="modal-right">
                    <h2 class="beat-title">Beat Funk MC Santana x MC Dayo</h2>
                    <p class="beat-desc">
                        Una fusión explosiva de ritmos cariocas con bajos 808 distorsionados. 
                        Diseñado para romper la pista de baile con una energía oscura y agresiva.
                    </p>

                    <h3 class="licenses-title">Selecciona tu Licencia</h3>
                    
                    <div class="pricing-cards">
                        <div class="price-card standard">
                            <div class="card-header">
                                <h4>Standard</h4>
                                <span class="price">$29.99</span>
                            </div>
                            <ul class="features">
                                <li>Archivo MP3</li>
                                <li>10k Streams</li>
                                <li>Sin Radio</li>
                            </ul>
                            <button @click="comprarBeat('Standard', 29.99)" class="buy-btn">COMPRAR</button>
                        </div>

                        <div class="price-card premium">
                            <div class="card-header">
                                <h4>Premium</h4>
                                <span class="price">$79.99</span>
                            </div>
                            <ul class="features">
                                <li>MP3 + WAV</li>
                                <li>500k Streams</li>
                                <li>Radio Regional</li>
                            </ul>
                            <button @click="comprarBeat('Premium', 79.99)" class="buy-btn">COMPRAR</button>
                        </div>

                        <div class="price-card exclusive">
                            <div class="card-header">
                                <h4>Exclusiva</h4>
                                <span class="price">$199.99</span>
                            </div>
                            <ul class="features">
                                <li>Trackouts (Stems)</li>
                                <li>Streams Ilimitados</li>
                                <li>Propiedad Total</li>
                            </ul>
                            <button @click="comprarBeat('Exclusiva', 199.99)" class="buy-btn gold">COMPRAR</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

  </div>
</template>

<script>
// --- CORRECCIÓN IMPORTANTE: USAR @ PARA LA RUTA ---
import beatDemo from '@/assets/beat_demo.mp3'

export default {
  data() {
    return {
      // Variable del audio
      audioSource: beatDemo,

      isAuthenticated: false,
      showRegister: false,
      form: { username: '', password: '' },
      currentUser: '',
      errorMessage: '',
      
      // Estado del Modal
      mostrarModal: false,
    };
  },
  mounted() {
    // Verificar sesión guardada
    const savedSession = localStorage.getItem('kairoUserSession');
    const savedUser = localStorage.getItem('kairoUserName');
    if (savedSession) {
      this.isAuthenticated = true;
      this.currentUser = savedUser || 'Usuario';
    }
  },
  methods: {
    toggleMode() {
      this.showRegister = !this.showRegister;
      this.errorMessage = '';
      this.form = { username: '', password: '' };
    },
    async handleSubmit() {
      const endpoint = this.showRegister ? 'http://localhost:5000/register' : 'http://localhost:5000/login';
      try {
        const response = await fetch(endpoint, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.form)
        });
        const data = await response.json();

        if (response.ok) {
          if (this.showRegister) {
            alert('Registro exitoso. Por favor inicia sesión.');
            this.toggleMode(); 
          } else {
            this.isAuthenticated = true;
            this.currentUser = this.form.username;
            localStorage.setItem('kairoUserSession', 'true');
            localStorage.setItem('kairoUserName', this.form.username);
          }
        } else {
          this.errorMessage = data.message;
        }
      } catch (error) {
        this.errorMessage = "Error de conexión. ¿Está corriendo 'python server.py'?";
      }
    },
    logout() {
      this.isAuthenticated = false;
      this.form = { username: '', password: '' };
      localStorage.removeItem('kairoUserSession');
      localStorage.removeItem('kairoUserName');
    },
    
    // --- Lógica del Modal ---
    abrirModalBeat() {
        this.mostrarModal = true;
    },
    cerrarModal() {
        this.mostrarModal = false;
        // Pausar audio al cerrar
        const audio = document.querySelector('audio');
        if(audio) audio.pause();
    },

    // --- Lógica de Compra y PDF ---
    async comprarBeat(licencia, precio) {
        if(!confirm(`¿Confirmar compra de licencia ${licencia} por $${precio}?`)) return;

        try {
            const response = await fetch('http://localhost:5000/comprar', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    titulo: "Beat Funk MC Santana",
                    precio: precio,
                    licencia: licencia,
                    usuario: this.currentUser
                })
            });

            if (response.ok) {
                const blob = await response.blob();
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = `Contrato_KairoWave_${licencia}.pdf`;
                document.body.appendChild(a);
                a.click();
                a.remove();
                alert("¡Compra exitosa! Contrato descargado.");
            } else {
                alert("Hubo un error al procesar la compra.");
            }
        } catch (error) {
            console.error(error);
            alert("Error conectando con el servidor.");
        }
    }
  }
};
</script>

<style scoped>
/* ========================================= */
/* ESTILOS DEL LOGIN                         */
/* ========================================= */
.auth-container {
  min-height: 80vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: radial-gradient(circle at center, #1a1a1d 0%, #000 100%);
  color: white;
  padding: 40px 20px;
}

.auth-box {
  background: #121212;
  padding: 40px;
  border-radius: 16px;
  width: 100%;
  max-width: 400px;
  box-shadow: 0 8px 30px rgba(0,0,0,0.5);
  border: 1px solid #333;
  text-align: center;
}

.auth-header-nav { display: flex; justify-content: flex-start; margin-bottom: 20px; }
.home-btn { text-decoration: none; color: #888; font-size: 0.9rem; display: flex; align-items: center; gap: 5px; transition: color 0.3s; }
.home-btn:hover { color: #b11db9; }

.auth-title { margin-bottom: 30px; font-family: 'Impact', sans-serif; letter-spacing: 1px; font-size: 2rem; }
.input-group { margin-bottom: 20px; text-align: left; }
.input-group label { display: block; margin-bottom: 8px; font-size: 0.9rem; color: #aaa; }
.input-group input { width: 100%; padding: 12px; background: #2a2a2a; border: 1px solid #444; border-radius: 6px; color: white; font-size: 1rem; }
.input-group input:focus { outline: none; border-color: #b11db9; }
.password-hint { font-size: 0.75rem; color: #888; margin-top: 5px; }
.auth-btn { width: 100%; padding: 12px; background: #b11db9; color: white; border: none; border-radius: 25px; font-size: 1rem; font-weight: bold; cursor: pointer; margin-top: 10px; transition: transform 0.2s; }
.auth-btn:hover { transform: scale(1.02); background: #b11db9; }
.toggle-auth { margin-top: 20px; font-size: 0.9rem; }
.toggle-auth span { color: #b11db9; cursor: pointer; font-weight: bold; margin-left: 5px; }
.error-msg { color: #ff4d4d; margin-top: 15px; font-size: 0.9rem; }

/* ========================================= */
/* ESTILOS DEL PERFIL                        */
/* ========================================= */
.logout-header { display: flex; justify-content: flex-end; padding: 20px 40px; }
.logout-btn { background: transparent; border: 1px solid #444; color: #fff; padding: 8px 16px; border-radius: 20px; cursor: pointer; transition: all 0.3s; }
.logout-btn:hover { background: #333; border-color: #fff; }

.section { padding: 20px 40px; margin-bottom: 40px; max-width: 1400px; margin-left: auto; margin-right: auto; }
.section-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; color: #fff; border-left: 4px solid #b11db9; padding-left: 15px; }
.section-header h2 { font-size: 1.5rem; font-weight: 700; margin: 0; }
.section-header i { font-size: 1.5rem; cursor: pointer; color: #b3b3b3; }

.project-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }

.project-card { height: 300px; border-radius: 12px; background-size: cover; background-position: center; position: relative; overflow: hidden; cursor: pointer; box-shadow: 0 4px 15px rgba(0,0,0,0.3); transition: transform 0.3s ease; }
.project-card:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.5); }
.project-info { position: absolute; bottom: 0; left: 0; width: 100%; padding: 15px; background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.6) 60%, transparent 100%); color: white; display: flex; flex-direction: column; justify-content: flex-end; }
.project-info h3 { margin: 0 0 5px 0; font-size: 1.1rem; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.project-info p { margin: 0 0 10px 0; font-size: 0.85rem; color: #ccc; }
.project-stats { display: flex; justify-content: space-between; align-items: center; font-size: 0.8rem; color: #b11db9; font-weight: bold; }

.profile-header-modern { position: relative; background-image: url('/assets/kairoProyect1.jpg'); background-size: cover; background-position: center 30%; height: 350px; border-radius: 20px; display: flex; align-items: flex-end; padding: 40px; margin: 0 40px 80px 40px; box-shadow: inset 0 -150px 100px -20px rgba(0,0,0,0.7); }
.header-content { width: 100%; display: flex; justify-content: space-between; align-items: flex-end; max-width: 1400px; margin: 0 auto; }
.text-info { max-width: 60%; }
.artist-name { font-family: 'Impact', sans-serif; font-size: 5rem; color: #fff; line-height: 1; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 2px; text-shadow: 4px 4px 8px rgba(0, 0, 0, 0.9); }
.artist-bio { color: #f0f0f0; font-size: 1.2rem; font-style: italic; font-weight: 300; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); }
.profile-pic-container { position: absolute; right: 80px; bottom: -60px; }
.profile-img { width: 200px; height: 200px; object-fit: cover; border-radius: 50%; border: 8px solid #0b0b0f; box-shadow: 0 10px 25px rgba(0,0,0,0.6); }

/* ========================================= */
/* ESTILOS DEL MODAL (VENTANA EMERGENTE)     */
/* ========================================= */
.modal-overlay {
    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0, 0, 0, 0.85); backdrop-filter: blur(5px);
    z-index: 2000; display: flex; justify-content: center; align-items: center; padding: 20px;
}
.modal-content {
    background: #121212; width: 100%; max-width: 1000px;
    border-radius: 20px; border: 1px solid #333;
    box-shadow: 0 10px 40px rgba(0,0,0,0.8);
    position: relative; overflow: hidden; max-height: 90vh; overflow-y: auto;
}
.close-modal {
    position: absolute; top: 15px; right: 20px; background: none; border: none;
    color: #fff; font-size: 2rem; cursor: pointer; z-index: 10;
}
.modal-grid { display: grid; grid-template-columns: 350px 1fr; gap: 0; }

.modal-left {
    background: #0b0b0f; padding: 30px; display: flex; flex-direction: column; align-items: center; border-right: 1px solid #222;
}
.modal-img { width: 100%; border-radius: 12px; box-shadow: 0 5px 20px rgba(0,0,0,0.5); margin-bottom: 20px; }
.audio-player-container { width: 100%; margin-bottom: 30px; text-align: center; }
.audio-label { color: #888; font-size: 0.8rem; margin-bottom: 5px; text-transform: uppercase; letter-spacing: 1px; }
.custom-audio { width: 100%; height: 40px; border-radius: 20px; }
.beat-details { width: 100%; text-align: left; background: #1a1a1d; padding: 20px; border-radius: 10px; }
.beat-details h4 { color: #fff; margin-bottom: 10px; font-size: 1rem; border-bottom: 1px solid #333; padding-bottom: 5px; }
.beat-details ul { list-style: none; padding: 0; }
.beat-details li { color: #ccc; font-size: 0.9rem; margin-bottom: 8px; display: flex; justify-content: space-between; }
.beat-details li strong { color: #b11db9; }

.modal-right { padding: 40px; }
.beat-title { font-family: 'Impact', sans-serif; font-size: 2.5rem; color: #fff; margin-bottom: 15px; letter-spacing: 1px; }
.beat-desc { color: #bbb; line-height: 1.6; margin-bottom: 30px; font-size: 1rem; }
.licenses-title { color: #fff; margin-bottom: 20px; font-size: 1.2rem; text-transform: uppercase; border-left: 4px solid #b11db9; padding-left: 10px; }

.pricing-cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; }
.price-card {
    background: #1a1a1d; border: 1px solid #333; border-radius: 10px; padding: 20px; text-align: center;
    transition: transform 0.3s, border-color 0.3s; display: flex; flex-direction: column; justify-content: space-between;
}
.price-card:hover { transform: translateY(-5px); border-color: #b11db9; }
.price-card.exclusive:hover { border-color: #ffd700; }
.card-header h4 { color: #fff; margin: 0; font-size: 1.1rem; }
.price { display: block; font-size: 1.5rem; color: #fff; font-weight: bold; margin: 10px 0; }
.features { list-style: none; padding: 0; margin: 15px 0; color: #888; font-size: 0.85rem; text-align: left; }
.features li { margin-bottom: 5px; border-bottom: 1px solid #2a2a2a; padding-bottom: 5px; }
.buy-btn {
    background: transparent; border: 1px solid #b11db9; color: #b11db9; padding: 10px;
    border-radius: 20px; font-weight: bold; cursor: pointer; transition: all 0.3s; width: 100%;
}
.buy-btn:hover { background: #b11db9; color: #fff; }
.buy-btn.gold { border-color: #ffd700; color: #ffd700; }
.buy-btn.gold:hover { background: #ffd700; color: #000; }

/* ========================================= */
/* RESPONSIVE (MÓVIL / iPHONE)               */
/* ========================================= */
@media (max-width: 768px) {
  /* Cabecera */
  .profile-header-modern { flex-direction: column; height: auto; min-height: 400px; padding: 30px 20px 90px 20px; margin: 0 10px 60px 10px; align-items: center; text-align: center; background-position: center top; }
  .header-content { flex-direction: column; align-items: center; }
  .text-info { max-width: 100%; margin-bottom: 20px; }
  .artist-name { font-size: 3rem; }
  .profile-pic-container { right: auto; left: 50%; transform: translateX(-50%); bottom: -50px; }
  .profile-img { width: 160px; height: 160px; }

  /* Secciones y Grid */
  .project-grid { grid-template-columns: 1fr; gap: 25px; }
  .section { padding: 20px 15px; }

  /* Login */
  .auth-box { width: 90%; padding: 30px 20px; }
  .logout-header { padding: 10px 20px; }

  /* Modal */
  .modal-grid { grid-template-columns: 1fr; }
  .modal-left { border-right: none; border-bottom: 1px solid #222; }
  .pricing-cards { grid-template-columns: 1fr; }
  .beat-title { font-size: 1.8rem; }
}
</style>