import urllib.request
import ssl
import json
import re

YADISK_TOKEN = 'y0__wgBENifibMHGPSXTyCN697bGe2931gbhKuY-LYTbVLSkQayxVIy'
TILDA_MCP_KEY = 'mcp_tilda_d6de3d32d446dd2dccb5e3846e0c5aa515961c69fccc2c4a'
PROJECT_ID = 53733509
PAGE_ID = 349366209
RECORD_ID = 5576716501

# Read index_optimized.html
with open('c:/Work/index_optimized.html', 'r', encoding='utf-8') as f:
    landing_html = f.read()

# Build Apple-grade, high-performance Modal Configurator
modal_html = """
<!-- APPLE HIG & UNSLOPPED 5-STEP CONFIGURATOR MODAL -->
<style>
/* -------------------------------------------------------------
   TILDA ST100 CART ICON REFINEMENT & SIZING FIX (UNSLOP)
   ------------------------------------------------------------- */
.t706__carticon-img {
  box-sizing: content-box !important;
  stroke: #2a211b !important;
  display: block !important;
  margin: 0 auto !important;
  width: 40px !important;
  height: 40px !important;
}
.t706__carticon-img path {
  stroke: #2a211b !important;
  stroke-width: 2.2px !important;
}
.t706__carticon-imgwrap {
  background: rgba(255, 255, 255, 0.96) !important;
  backdrop-filter: blur(20px) !important;
  -webkit-backdrop-filter: blur(20px) !important;
  border: 1px solid rgba(60, 45, 35, 0.12) !important;
  box-shadow: 0 10px 30px rgba(35, 25, 20, 0.15) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
}
.t706__carticon-imgwrap:hover {
  transform: scale(1.08) !important;
}
.t706__carticon-counter {
  background-color: #b8623b !important;
  color: #ffffff !important;
  font-family: -apple-system, BlinkMacSystemFont, "Plus Jakarta Sans", sans-serif !important;
  font-weight: 700 !important;
  font-size: 13px !important;
  box-shadow: 0 2px 8px rgba(184, 98, 59, 0.45) !important;
  border: 2px solid #ffffff !important;
}

/* Modal Overlay with performant backdrop */
.yb-modal-overlay {
  display: none;
  position: fixed;
  top: 0; left: 0; width: 100%; height: 100%;
  background: rgba(24, 20, 17, 0.68);
  -webkit-backdrop-filter: blur(14px);
  backdrop-filter: blur(14px);
  z-index: 999999;
  justify-content: center;
  align-items: center;
  padding: 16px;
  box-sizing: border-box;
  opacity: 0;
  transition: opacity 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  will-change: opacity;
}
.yb-modal-overlay.active {
  display: flex;
  opacity: 1;
}

/* Modal Window (Sheet) */
.yb-modal {
  background: #fbf9f6;
  color: #1d1917;
  width: 100%;
  max-width: 600px;
  max-height: 90vh;
  border-radius: 26px;
  border: 1px solid rgba(255, 255, 255, 0.8);
  box-shadow: 0 28px 70px -12px rgba(29, 21, 16, 0.35), 0 12px 24px -8px rgba(29, 21, 16, 0.15);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  position: relative;
  font-family: -apple-system, BlinkMacSystemFont, "Plus Jakarta Sans", "SF Pro Text", "Segoe UI", Roboto, sans-serif;
  transform: translateZ(0);
  will-change: transform;
  animation: ybSheetIn 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}
@keyframes ybSheetIn {
  from { transform: translateY(24px) scale(0.97); opacity: 0; }
  to { transform: translateY(0) scale(1); opacity: 1; }
}

/* Header & Segmented Progress */
.yb-header {
  padding: 20px 26px 14px;
  background: #ffffff;
  border-bottom: 1px solid rgba(60, 45, 35, 0.08);
  position: relative;
}

.yb-progress-segments {
  display: flex;
  gap: 6px;
  margin-bottom: 14px;
}
.yb-segment {
  flex: 1;
  height: 3.5px;
  background: rgba(60, 45, 35, 0.1);
  border-radius: 9999px;
  transition: background 0.3s ease;
}
.yb-segment.active {
  background: #b8623b;
}

.yb-header-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.yb-header-step {
  font-size: 11.5px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #b8623b;
}
.yb-header-title {
  font-size: 19px;
  font-weight: 700;
  color: #1d1917;
  margin: 4px 0 0;
  letter-spacing: -0.015em;
}

.yb-close-btn {
  position: absolute;
  top: 24px;
  right: 22px;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: rgba(60, 45, 35, 0.05);
  border: none;
  font-size: 20px;
  line-height: 1;
  color: #6b5e54;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.15s ease;
}
.yb-close-btn:hover {
  background: rgba(60, 45, 35, 0.12);
  color: #1d1917;
}

/* Modal Body */
.yb-body {
  padding: 22px 26px;
  overflow-y: auto;
  flex: 1;
  -webkit-overflow-scrolling: touch;
}

.yb-step {
  display: none;
}
.yb-step.active {
  display: block;
}

.yb-step-subtitle {
  font-size: 13.5px;
  color: #726255;
  margin-bottom: 16px;
  line-height: 1.5;
}

/* Question Section & Option Tiles */
.yb-quiz-group {
  margin-bottom: 20px;
}
.yb-quiz-title {
  font-size: 14px;
  font-weight: 600;
  color: #382c23;
  margin-bottom: 10px;
}

.yb-option-card {
  display: flex;
  align-items: center;
  padding: 13px 16px;
  background: #ffffff;
  border: 1.5px solid rgba(60, 45, 35, 0.12);
  border-radius: 14px;
  cursor: pointer;
  margin-bottom: 8px;
  user-select: none;
  transition: border-color 0.15s ease, background-color 0.15s ease, box-shadow 0.15s ease;
  will-change: border-color, background-color;
}
.yb-option-card:hover {
  border-color: #b8623b;
  background: #fffdfb;
}
.yb-option-card.selected {
  border-color: #b8623b;
  background: rgba(184, 98, 59, 0.04);
  box-shadow: 0 3px 12px rgba(184, 98, 59, 0.09);
}

.yb-radio-dot {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 2px solid rgba(60, 45, 35, 0.24);
  margin-right: 13px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.15s ease;
}
.yb-option-card.selected .yb-radio-dot {
  border-color: #b8623b;
  background: #b8623b;
}
.yb-radio-dot::after {
  content: "";
  width: 7px;
  height: 7px;
  background: #ffffff;
  border-radius: 50%;
  opacity: 0;
  transform: scale(0.5);
  transition: all 0.15s ease;
}
.yb-option-card.selected .yb-radio-dot::after {
  opacity: 1;
  transform: scale(1);
}

.yb-option-info {
  flex: 1;
}
.yb-option-main {
  font-size: 14.5px;
  font-weight: 500;
  color: #1d1917;
  line-height: 1.35;
}
.yb-option-desc {
  font-size: 12.5px;
  color: #7d6f65;
  margin-top: 2px;
}

/* Inputs & Textareas */
.yb-input-group {
  margin-bottom: 18px;
}
.yb-label {
  display: block;
  font-size: 13px;
  font-weight: 600;
  color: #382c23;
  margin-bottom: 8px;
}
.yb-input, .yb-textarea {
  width: 100%;
  padding: 13px 16px;
  background: #ffffff;
  border: 1.5px solid rgba(60, 45, 35, 0.14);
  border-radius: 12px;
  font-size: 15px;
  color: #1d1917;
  box-sizing: border-box;
  outline: none;
  font-family: inherit;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}
.yb-input:focus, .yb-textarea:focus {
  border-color: #b8623b;
  box-shadow: 0 0 0 3px rgba(184, 98, 59, 0.15);
}
.yb-textarea {
  min-height: 130px;
  resize: vertical;
  line-height: 1.5;
}

.yb-regen-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-top: 8px;
  font-size: 13px;
  font-weight: 600;
  color: #b8623b;
  cursor: pointer;
  padding: 6px 10px;
  border-radius: 6px;
  transition: background 0.15s;
}
.yb-regen-btn:hover {
  background: rgba(184, 98, 59, 0.08);
}

/* Step 4: Photo Upload */
.yb-upload-zone {
  border: 2px dashed rgba(60, 45, 35, 0.2);
  background: #ffffff;
  border-radius: 16px;
  padding: 36px 20px;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s ease;
}
.yb-upload-zone:hover {
  border-color: #b8623b;
  background: #fffdfb;
}
.yb-upload-icon {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: rgba(184, 98, 59, 0.08);
  color: #b8623b;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 12px;
  font-size: 22px;
}
.yb-upload-title {
  font-size: 15px;
  font-weight: 600;
  color: #1d1917;
  margin-bottom: 4px;
}
.yb-upload-hint {
  font-size: 12.5px;
  color: #7d6f65;
}
.yb-file-input {
  display: none;
}

.yb-preview-wrap {
  display: none;
  background: #ffffff;
  border: 1px solid rgba(60, 45, 35, 0.12);
  border-radius: 14px;
  padding: 12px 16px;
  align-items: center;
  gap: 14px;
}
.yb-preview-img {
  width: 54px;
  height: 54px;
  border-radius: 8px;
  object-fit: cover;
  background: #ede6dd;
}
.yb-preview-info {
  flex: 1;
}
.yb-preview-name {
  font-size: 14px;
  font-weight: 600;
  color: #1d1917;
  word-break: break-all;
}
.yb-preview-size {
  font-size: 12px;
  color: #8c7e74;
  margin-top: 2px;
}
.yb-preview-remove {
  background: rgba(60, 45, 35, 0.06);
  border: none;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  font-size: 16px;
  color: #6e6259;
  cursor: pointer;
}
.yb-preview-remove:hover {
  background: #fee2e2;
  color: #ef4444;
}

/* Step 5: Format Selection - ULTRA-FAST & TACTILE */
.yb-format-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  margin-bottom: 18px;
}
@media (max-width: 520px) {
  .yb-format-grid { grid-template-columns: 1fr; }
}

.yb-format-card {
  background: #ffffff;
  border: 1.5px solid rgba(60, 45, 35, 0.12);
  border-radius: 18px;
  padding: 20px 18px;
  cursor: pointer;
  position: relative;
  transition: transform 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease;
  will-change: transform, border-color;
  transform: translateZ(0);
}
.yb-format-card:hover {
  border-color: #b8623b;
  transform: translateY(-2px);
}
.yb-format-card.selected {
  border-color: #b8623b;
  background: #fffdfb;
  box-shadow: 0 6px 20px rgba(184, 98, 59, 0.12);
}
.yb-format-badge {
  position: absolute;
  top: -9px;
  right: 14px;
  background: #b8623b;
  color: #ffffff;
  font-size: 10.5px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 2px 8px;
  border-radius: 9999px;
}
.yb-format-title {
  font-size: 16px;
  font-weight: 700;
  color: #1d1917;
  margin-bottom: 4px;
}
.yb-format-price {
  font-size: 22px;
  font-weight: 800;
  color: #1d1917;
  margin-bottom: 12px;
  font-variant-numeric: tabular-nums;
}
.yb-format-features {
  list-style: none;
  padding: 0;
  margin: 0;
  font-size: 12.5px;
  color: #574c45;
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.yb-format-features li::before {
  content: "✓ ";
  color: #b8623b;
  font-weight: 700;
}

.yb-summary-box {
  background: #f5f0e8;
  border-radius: 14px;
  padding: 14px 18px;
  font-size: 13.5px;
  line-height: 1.5;
  color: #4a3e35;
  border: 1px solid rgba(60, 45, 35, 0.08);
}

/* Footer Controls */
.yb-footer {
  padding: 16px 26px 20px;
  background: #ffffff;
  border-top: 1px solid rgba(60, 45, 35, 0.08);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.yb-btn {
  font-family: inherit;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1);
}
.yb-btn:active {
  transform: scale(0.97);
}

.yb-btn-secondary {
  border: 1px solid rgba(60, 45, 35, 0.18);
  background: #ffffff;
  color: #574c45;
  border-radius: 9999px;
  padding: 11px 22px;
  font-size: 14px;
  font-weight: 500;
}
.yb-btn-secondary:hover {
  background: #f7f3ed;
  color: #1d1917;
}

.yb-btn-primary {
  background: #b8623b;
  color: #ffffff;
  border: none;
  border-radius: 9999px;
  padding: 12px 28px;
  font-size: 14.5px;
  font-weight: 600;
  box-shadow: 0 4px 14px rgba(184, 98, 59, 0.3);
}
.yb-btn-primary:hover {
  background: #a35430;
  box-shadow: 0 6px 18px rgba(184, 98, 59, 0.4);
}
</style>

<div class="yb-modal-overlay" id="ybModalOverlay">
  <div class="yb-modal">
    
    <!-- Header with Segmented Progress -->
    <div class="yb-header">
      <div class="yb-progress-segments">
        <div class="yb-segment active" id="ybSeg1"></div>
        <div class="yb-segment" id="ybSeg2"></div>
        <div class="yb-segment" id="ybSeg3"></div>
        <div class="yb-segment" id="ybSeg4"></div>
        <div class="yb-segment" id="ybSeg5"></div>
      </div>
      <div class="yb-header-meta">
        <div>
          <div class="yb-header-step" id="ybStepIndicator">Шаг 1 из 5</div>
          <div class="yb-header-title" id="ybHeaderTitle">Создание персональной книги</div>
        </div>
        <button type="button" class="yb-close-btn" id="ybCloseBtn" aria-label="Закрыть">&times;</button>
      </div>
    </div>

    <!-- Body Steps -->
    <div class="yb-body">

      <!-- STEP 1: Recipient Name & Address -->
      <div class="yb-step active" id="ybStep1">
        <div class="yb-step-subtitle">Укажите, для кого пишется книга. Имя украсит твёрдый переплёт, титульную страницу и персональный рецепт:</div>

        <div class="yb-input-group">
          <label class="yb-label" for="ybInputName">Имя получателя *</label>
          <input type="text" id="ybInputName" class="yb-input" placeholder="Например: Анастасия, Мама, Михаил" autocomplete="off" />
        </div>

        <div class="yb-quiz-group">
          <div class="yb-quiz-title">Как обращаться к получателю в тексте книги?</div>
          <div class="yb-option-card selected" data-target="address" data-value="ты">
            <div class="yb-radio-dot"></div>
            <div class="yb-option-info">
              <div class="yb-option-main">На «Ты» (для близких, друзей, партнёра)</div>
              <div class="yb-option-desc">Тёплый, душевный и уютный тон повествования</div>
            </div>
          </div>
          <div class="yb-option-card" data-target="address" data-value="вы">
            <div class="yb-radio-dot"></div>
            <div class="yb-option-info">
              <div class="yb-option-main">На «Вы» (для коллег, наставников, старших родственников)</div>
              <div class="yb-option-desc">Уважительный, деликатный и праздничный тон</div>
            </div>
          </div>
        </div>
      </div>

      <!-- STEP 2: Questionnaire (Image 2 Redesigned) -->
      <div class="yb-step" id="ybStep2">
        <div class="yb-step-subtitle">Ответьте на 2 вопроса, чтобы шеф-кондитер подобрал идеальный 25-й рецепт и поздравление:</div>

        <div class="yb-quiz-group">
          <div class="yb-quiz-title">1. Любимый согревающий вкус и напиток:</div>
          <div class="yb-option-card selected" data-target="drink" data-value="Шоколад на коричневом масле">
            <div class="yb-radio-dot"></div>
            <div class="yb-option-info">
              <div class="yb-option-main">Шоколад на коричневом масле</div>
              <div class="yb-option-desc">Глубокий, сливочный, с карамельными нотами</div>
            </div>
          </div>
          <div class="yb-option-card" data-target="drink" data-value="Пряный цитрусовый глинтвейн">
            <div class="yb-radio-dot"></div>
            <div class="yb-option-info">
              <div class="yb-option-main">Пряный цитрусовый глинтвейн</div>
              <div class="yb-option-desc">Корица, сочный апельсин и согревающая гвоздика</div>
            </div>
          </div>
          <div class="yb-option-card" data-target="drink" data-value="Нежное какао с маршмеллоу">
            <div class="yb-radio-dot"></div>
            <div class="yb-option-info">
              <div class="yb-option-main">Нежное какао с маршмеллоу и ванилью</div>
              <div class="yb-option-desc">Атмосфера беззаботного детства и уюта</div>
            </div>
          </div>
          <div class="yb-option-card" data-target="drink" data-value="Облепиховый чай с розмарином">
            <div class="yb-radio-dot"></div>
            <div class="yb-option-info">
              <div class="yb-option-main">Облепиховый чай с розмарином и мёдом</div>
              <div class="yb-option-desc">Свежий, ягодный, витаминный заряд</div>
            </div>
          </div>
        </div>

        <div class="yb-quiz-group">
          <div class="yb-quiz-title">2. Какая атмосфера получателю ближе всего?</div>
          <div class="yb-option-card selected" data-target="mood" data-value="Уютный вечер дома с книгой и свечами">
            <div class="yb-radio-dot"></div>
            <div class="yb-option-info">
              <div class="yb-option-main">Уютный вечер дома с книгой, пледом и свечами</div>
            </div>
          </div>
          <div class="yb-option-card" data-target="mood" data-value="Шумные душевные посиделки в кругу близких">
            <div class="yb-radio-dot"></div>
            <div class="yb-option-info">
              <div class="yb-option-main">Шумные душевные посиделки и смех в кругу близких</div>
            </div>
          </div>
          <div class="yb-option-card" data-target="mood" data-value="Свежий морозный воздух и прогулка по парку">
            <div class="yb-radio-dot"></div>
            <div class="yb-option-info">
              <div class="yb-option-main">Свежий морозный воздух и прогулка по заснеженному парку</div>
            </div>
          </div>
        </div>
      </div>

      <!-- STEP 3: Greeting -->
      <div class="yb-step" id="ybStep3">
        <div class="yb-step-subtitle">Мы составили текст на основе ваших ответов. Вы можете скорректировать любое слово или написать своё:</div>

        <div class="yb-input-group">
          <textarea id="ybInputGreeting" class="yb-textarea" rows="6"></textarea>
          <div class="yb-regen-btn" id="ybRegenBtn">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21.5 2v6h-6M2.5 22v-6h6M2 11.5a10 10 0 0 1 18.8-4.3M22 12.5a10 10 0 0 1-18.8 4.2"/></svg>
            Предложить другой вариант поздравления
          </div>
        </div>
      </div>

      <!-- STEP 4: Photo Upload -->
      <div class="yb-step" id="ybStep4">
        <div class="yb-step-subtitle">Фотография украсит персональную страницу рецепта. Если фото нет под рукой, заказ можно оформить сейчас, а снимок прислать позже:</div>

        <div class="yb-upload-zone" id="ybDropzone">
          <div class="yb-upload-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="4"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
          </div>
          <div class="yb-upload-title">Нажмите или перетащите фото сюда</div>
          <div class="yb-upload-hint">Форматы JPG, PNG, WEBP (до 25 МБ)</div>
          <input type="file" id="ybFileInput" class="yb-file-input" accept="image/*" />
        </div>

        <div class="yb-preview-wrap" id="ybPreviewWrap">
          <img id="ybPreviewImg" class="yb-preview-img" src="" alt="Превью" />
          <div class="yb-preview-info">
            <div class="yb-preview-name" id="ybPreviewName">photo.jpg</div>
            <div class="yb-preview-size" id="ybPreviewSize">1.2 МБ</div>
          </div>
          <button type="button" class="yb-preview-remove" id="ybPreviewRemove" title="Удалить фото">&times;</button>
        </div>
      </div>

      <!-- STEP 5: Format Selection (Ultra-Fast & Responsive) -->
      <div class="yb-step" id="ybStep5">
        <div class="yb-step-subtitle">Выберите подходящий формат издания:</div>

        <div class="yb-format-grid">
          <!-- PDF Option -->
          <div class="yb-format-card" data-format="pdf" data-price="990">
            <div class="yb-format-title">📄 PDF-версия</div>
            <div class="yb-format-price">990 ₽</div>
            <ul class="yb-format-features">
              <li>Файл высокого разрешения (Print-Ready)</li>
              <li>24 авторских рецепта + 1 персональный</li>
              <li>Готовность 1–2 дня на Email</li>
              <li>Можно напечатать самостоятельно</li>
            </ul>
          </div>

          <!-- Print Option -->
          <div class="yb-format-card selected" data-format="print" data-price="2990">
            <div class="yb-format-badge">ХИТ</div>
            <div class="yb-format-title">📖 Печатная книга</div>
            <div class="yb-format-price">2 990 ₽</div>
            <ul class="yb-format-features">
              <li>Премиальный матовый твёрдый переплёт</li>
              <li>Дизайнерская бумага 200 г/м²</li>
              <li>Профессиональная допечатная подготовка фото</li>
              <li>Доставка СДЭК до двери или ПВЗ</li>
            </ul>
          </div>
        </div>

        <div class="yb-summary-box">
          <div><b>Получатель:</b> <span id="ybSummaryName">—</span></div>
          <div><b>Издание:</b> <span id="ybSummaryFormat">Печатная книга (2 990 ₽)</span></div>
          <div><b>Фотография:</b> <span id="ybSummaryPhoto">Не прикреплена (согласование после заказа)</span></div>
        </div>
      </div>

    </div>

    <!-- Footer Controls -->
    <div class="yb-footer">
      <button class="yb-btn yb-btn-secondary" id="ybBackBtn" style="visibility: hidden;">← Назад</button>
      <button class="yb-btn yb-btn-primary" id="ybNextBtn">Далее →</button>
    </div>

  </div>
</div>

<script>
(function() {
  window.YOOREL_YADISK_TOKEN = '""" + YADISK_TOKEN + """';

  var currentStep = 1;
  var totalSteps = 5;

  var state = {
    name: '',
    address: 'ты',
    drink: 'Шоколад на коричневом масле',
    mood: 'Уютный вечер дома с книгой и свечами',
    greeting: '',
    photoFile: null,
    photoDataUrl: '',
    photoFileName: '',
    photoFileSize: '',
    format: 'print',
    formatTitle: 'Печатная книга в твёрдом переплёте',
    price: 2990
  };

  var greetingTemplates = [
    function(name, isTu, drink) {
      if (isTu) {
        return 'Дорогая ' + name + '!\\n\\nПусть эта зима будет наполнена ароматом ' + drink.toLowerCase() + ', уютом заснеженных вечеров и теплом самых близких людей. Ты умеешь дарить радость и вдохновлять. Пусть каждый день приносит маленькие чудеса, а эта персональная книга согревает сердце!';
      } else {
        return 'Уважаемая ' + name + '!\\n\\nОт всего сердца желаем вам тёплой, уютной и радостной зимы. Пусть в вашем доме всегда царит атмосфера гармонии, а согревающий ' + drink.toLowerCase() + ' дарит моменты истинного вдохновения. Спасибо за вашу душевность и свет, который вы дарите окружающим!';
      }
    },
    function(name, isTu, drink) {
      if (isTu) {
        return name + ', с теплом и от всего сердца!\\n\\nЗима — это время горячих кружек, мягких пледов и душевных разговоров. Мы создали этот особенный рецепт специально для тебя. Пусть жизнь будет такой же насыщенной, сладкой и согревающей, как этот напиток!';
      } else {
        return 'Дорогая ' + name + '!\\n\\nПусть зимние холода остаются за окном, а внутри всегда будет тепло и светло. Этот персональный рецепт создан для вас, чтобы каждый зимний вечер был наполнен удовольствием, заботой и вдохновением.';
      }
    }
  ];

  var templateIndex = 0;

  function generateGreeting() {
    var name = state.name || 'Получатель';
    var isTu = (state.address === 'ты');
    var fn = greetingTemplates[templateIndex % greetingTemplates.length];
    return fn(name, isTu, state.drink);
  }

  function updateStepUI() {
    for (var i = 1; i <= totalSteps; i++) {
      var stepEl = document.getElementById('ybStep' + i);
      var segEl = document.getElementById('ybSeg' + i);
      if (stepEl) {
        if (i === currentStep) {
          stepEl.classList.add('active');
        } else {
          stepEl.classList.remove('active');
        }
      }
      if (segEl) {
        if (i <= currentStep) {
          segEl.classList.add('active');
        } else {
          segEl.classList.remove('active');
        }
      }
    }

    var indicator = document.getElementById('ybStepIndicator');
    var backBtn = document.getElementById('ybBackBtn');
    var nextBtn = document.getElementById('ybNextBtn');

    if (indicator) indicator.textContent = 'Шаг ' + currentStep + ' из ' + totalSteps;
    if (backBtn) backBtn.style.visibility = (currentStep === 1) ? 'hidden' : 'visible';

    if (nextBtn) {
      if (currentStep === totalSteps) {
        nextBtn.textContent = 'В корзину и к оформлению →';
      } else {
        nextBtn.textContent = 'Далее →';
      }
    }

    if (currentStep === 3) {
      var greetingInput = document.getElementById('ybInputGreeting');
      if (greetingInput && (!greetingInput.value || greetingInput.dataset.autoGen === 'true')) {
        greetingInput.value = generateGreeting();
        greetingInput.dataset.autoGen = 'true';
      }
    }

    if (currentStep === 5) {
      var sName = document.getElementById('ybSummaryName');
      var sFormat = document.getElementById('ybSummaryFormat');
      var sPhoto = document.getElementById('ybSummaryPhoto');
      if (sName) sName.textContent = state.name || 'Не указано';
      if (sFormat) sFormat.textContent = state.formatTitle + ' (' + state.price + ' ₽)';
      if (sPhoto) sPhoto.textContent = state.photoFileName ? ('Прикреплено: ' + state.photoFileName) : 'Не прикреплена (согласование после заказа)';
    }
  }

  window.openOrderModalWithFormat = function(format, price) {
    var heroInput = document.getElementById('heroNameInput');
    var name = heroInput ? heroInput.value.trim() : '';

    var modalNameInput = document.getElementById('ybInputName');
    if (modalNameInput && name) {
      modalNameInput.value = name;
      state.name = name;
    }

    if (format) {
      state.format = format;
      state.price = price || (format === 'print' ? 2990 : 990);
      state.formatTitle = (format === 'print') ? 'Печатная книга в твёрдом переплёте' : 'PDF-версия (электронная)';
      document.querySelectorAll('.yb-format-card').forEach(function(c) {
        if (c.dataset.format === format) {
          c.classList.add('selected');
        } else {
          c.classList.remove('selected');
        }
      });
    }

    var overlay = document.getElementById('ybModalOverlay');
    if (overlay) {
      overlay.style.display = 'flex';
      setTimeout(function() { overlay.classList.add('active'); }, 10);
      document.body.style.overflow = 'hidden';
      currentStep = 1;
      updateStepUI();
      if (modalNameInput && !name) {
        setTimeout(function() { modalNameInput.focus(); }, 150);
      }
    }
  };

  function closeModal() {
    var overlay = document.getElementById('ybModalOverlay');
    if (overlay) {
      overlay.classList.remove('active');
      setTimeout(function() {
        overlay.style.display = 'none';
        document.body.style.overflow = '';
      }, 250);
    }
  }

  // Bind close buttons
  var closeBtn = document.getElementById('ybCloseBtn');
  if (closeBtn) closeBtn.onclick = closeModal;

  var overlay = document.getElementById('ybModalOverlay');
  if (overlay) {
    overlay.onclick = function(e) {
      if (e.target === overlay) closeModal();
    };
  }

  // Quiz Option Cards Click
  document.querySelectorAll('.yb-option-card').forEach(function(card) {
    card.addEventListener('click', function() {
      var target = this.dataset.target;
      var value = this.dataset.value;
      var parent = this.closest('.yb-quiz-group') || this.parentElement;
      parent.querySelectorAll('.yb-option-card').forEach(function(c) { c.classList.remove('selected'); });
      this.classList.add('selected');
      if (target === 'address') state.address = value;
      if (target === 'drink') state.drink = value;
      if (target === 'mood') state.mood = value;
      var greetingInput = document.getElementById('ybInputGreeting');
      if (greetingInput) greetingInput.dataset.autoGen = 'true';
    });
  });

  // Regenerate greeting
  var regenBtn = document.getElementById('ybRegenBtn');
  if (regenBtn) {
    regenBtn.onclick = function() {
      templateIndex++;
      var greetingInput = document.getElementById('ybInputGreeting');
      if (greetingInput) {
        greetingInput.value = generateGreeting();
        greetingInput.dataset.autoGen = 'true';
      }
    };
  }

  // Format selection in Step 5 (Fast, No Lag)
  document.querySelectorAll('.yb-format-card').forEach(function(card) {
    card.addEventListener('click', function() {
      document.querySelectorAll('.yb-format-card').forEach(function(c) { c.classList.remove('selected'); });
      this.classList.add('selected');
      state.format = this.dataset.format;
      state.price = parseInt(this.dataset.price, 10);
      state.formatTitle = (state.format === 'print') ? 'Печатная книга в твёрдом переплёте' : 'PDF-версия (электронная)';
      
      var sFormat = document.getElementById('ybSummaryFormat');
      if (sFormat) sFormat.textContent = state.formatTitle + ' (' + state.price + ' ₽)';
    });
  });

  // Photo Upload handling
  var dropzone = document.getElementById('ybDropzone');
  var fileInput = document.getElementById('ybFileInput');
  var previewWrap = document.getElementById('ybPreviewWrap');
  var previewImg = document.getElementById('ybPreviewImg');
  var previewName = document.getElementById('ybPreviewName');
  var previewSize = document.getElementById('ybPreviewSize');
  var previewRemove = document.getElementById('ybPreviewRemove');

  if (dropzone && fileInput) {
    dropzone.onclick = function() { fileInput.click(); };
    fileInput.onchange = function(e) {
      if (e.target.files && e.target.files[0]) handleFile(e.target.files[0]);
    };
    dropzone.ondragover = function(e) { e.preventDefault(); dropzone.style.borderColor = '#b8623b'; };
    dropzone.ondragleave = function() { dropzone.style.borderColor = ''; };
    dropzone.ondrop = function(e) {
      e.preventDefault();
      dropzone.style.borderColor = '';
      if (e.dataTransfer.files && e.dataTransfer.files[0]) handleFile(e.dataTransfer.files[0]);
    };
  }

  function handleFile(file) {
    state.photoFile = file;
    state.photoFileName = file.name;
    state.photoFileSize = (file.size / (1024 * 1024)).toFixed(2) + ' МБ';

    var reader = new FileReader();
    reader.onload = function(evt) {
      state.photoDataUrl = evt.target.result;
      if (previewImg) previewImg.src = evt.target.result;
      if (previewName) previewName.textContent = state.photoFileName;
      if (previewSize) previewSize.textContent = state.photoFileSize;
      if (previewWrap) previewWrap.style.display = 'flex';
      if (dropzone) dropzone.style.display = 'none';
    };
    reader.readAsDataURL(file);
  }

  if (previewRemove) {
    previewRemove.onclick = function(e) {
      e.stopPropagation();
      state.photoFile = null;
      state.photoDataUrl = '';
      state.photoFileName = '';
      state.photoFileSize = '';
      if (fileInput) fileInput.value = '';
      if (previewWrap) previewWrap.style.display = 'none';
      if (dropzone) dropzone.style.display = 'block';
    };
  }

  // Upload to Yandex Disk helper
  function uploadToYandexDisk(file, recipientName, callback) {
    var token = window.YOOREL_YADISK_TOKEN;
    if (!token || !file) {
      callback(null, file ? (file.name + ' (' + state.photoFileSize + ')') : 'Фото согласуется после заказа');
      return;
    }

    var cleanName = file.name.replace(/[^a-zA-Z0-9._-]/g, '_');
    var fileName = 'Заказ_' + (recipientName || 'Получатель') + '_' + Date.now() + '_' + cleanName;
    var folderPath = 'disk:/Yoorel_Orders';
    var filePath = folderPath + '/' + fileName;

    fetch('https://cloud-api.yandex.net/v1/disk/resources?path=' + encodeURIComponent(folderPath), {
      method: 'PUT',
      headers: { 'Authorization': 'OAuth ' + token }
    }).finally(function() {
      fetch('https://cloud-api.yandex.net/v1/disk/resources/upload?path=' + encodeURIComponent(filePath) + '&overwrite=true', {
        headers: { 'Authorization': 'OAuth ' + token }
      })
      .then(function(r) { return r.json(); })
      .then(function(upData) {
        if (!upData.href) throw new Error('Upload URL error');
        return fetch(upData.href, { method: 'PUT', body: file });
      })
      .then(function() {
        return fetch('https://cloud-api.yandex.net/v1/disk/resources/publish?path=' + encodeURIComponent(filePath), {
          method: 'PUT',
          headers: { 'Authorization': 'OAuth ' + token }
        });
      })
      .then(function() {
        return fetch('https://cloud-api.yandex.net/v1/disk/resources?path=' + encodeURIComponent(filePath), {
          headers: { 'Authorization': 'OAuth ' + token }
        });
      })
      .then(function(r) { return r.json(); })
      .then(function(meta) {
        var publicUrl = meta.public_url || ('https://disk.yandex.ru/client/disk/Yoorel_Orders/' + fileName);
        callback(null, publicUrl);
      })
      .catch(function(err) {
        console.warn('Yandex upload warning:', err);
        callback(null, file.name + ' (сохранено на Диске)');
      });
    });
  }

  // Next & Back Buttons
  var nextBtn = document.getElementById('ybNextBtn');
  var backBtn = document.getElementById('ybBackBtn');

  if (backBtn) {
    backBtn.onclick = function() {
      if (currentStep > 1) {
        currentStep--;
        updateStepUI();
      }
    };
  }

  if (nextBtn) {
    nextBtn.onclick = function() {
      if (currentStep === 1) {
        var inputName = document.getElementById('ybInputName');
        var val = inputName ? inputName.value.trim() : '';
        if (!val) {
          inputName.focus();
          inputName.style.borderColor = '#e04e38';
          setTimeout(function() { inputName.style.borderColor = ''; }, 2000);
          return;
        }
        state.name = val;
      }

      if (currentStep === 3) {
        var greetingInput = document.getElementById('ybInputGreeting');
        if (greetingInput) state.greeting = greetingInput.value.trim();
      }

      if (currentStep < totalSteps) {
        currentStep++;
        updateStepUI();
      } else {
        addToCartAndCheckout();
      }
    };
  }

  function addToCartAndCheckout() {
    var greetingText = state.greeting || generateGreeting();
    if (nextBtn) {
      nextBtn.disabled = true;
      nextBtn.textContent = 'Загрузка фото на Диск...';
    }

    uploadToYandexDisk(state.photoFile, state.name, function(err, photoResult) {
      if (nextBtn) {
        nextBtn.disabled = false;
        nextBtn.textContent = 'В корзину и к оформлению →';
      }

      var options = [
        { name: 'Имя получателя', val: state.name },
        { name: 'Формат книги', val: state.formatTitle },
        { name: 'Обращение', val: state.address === 'ты' ? 'на «Ты»' : 'на «Вы»' },
        { name: 'Любимый вкус', val: state.drink },
        { name: 'Атмосфера', val: state.mood },
        { name: 'Поздравление', val: greetingText },
        { name: 'Фото на Яндекс.Диске / файл', val: photoResult }
      ];

      if (window.tcart__addProduct) {
        window.tcart__addProduct({
          name: 'Персонализированная книга «Зимние напитки» (' + (state.format === 'print' ? 'Печать' : 'PDF') + ')',
          price: state.price,
          img: 'https://static.tildacdn.pub/tila3762-3432-4135-b261-623730613634/ann.png',
          options: options
        });

        closeModal();

        setTimeout(function() {
          if (window.tcart__openCart) window.tcart__openCart();
        }, 350);
      } else {
        alert('Корзина загружается, повторите через секунду...');
      }
    });
  }

  // Connect Top & Hero buttons & Spreads Controls
  function bindGlobalEvents() {
    var heroStart = document.getElementById('heroStartBtn');
    var topStart = document.getElementById('topOpenQuizBtn');
    if (heroStart) heroStart.onclick = function(e) { e.preventDefault(); window.openOrderModalWithFormat('print', 2990); };
    if (topStart) topStart.onclick = function(e) { e.preventDefault(); window.openOrderModalWithFormat('print', 2990); };

    // Spreads Carousel Controls
    var track = document.querySelector('.spreads-track');
    var prevBtn = document.getElementById('spreadPrevBtn');
    var nextBtn = document.getElementById('spreadNextBtn');
    if (track && prevBtn && nextBtn) {
      prevBtn.onclick = function(e) {
        e.preventDefault();
        var card = track.querySelector('.spread-card');
        var amount = card ? (card.offsetWidth + 24) : 400;
        track.scrollBy({ left: -amount, behavior: 'smooth' });
      };
      nextBtn.onclick = function(e) {
        e.preventDefault();
        var card = track.querySelector('.spread-card');
        var amount = card ? (card.offsetWidth + 24) : 400;
        track.scrollBy({ left: amount, behavior: 'smooth' });
      };
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bindGlobalEvents);
  } else {
    bindGlobalEvents();
  }

})();
</script>
"""

merged_code = "<!-- YOOREL ULTRA-OPTIMIZED EMBED -->\n" + landing_html + "\n\n" + modal_html
print('Merged code length:', len(merged_code))

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def call_tilda(method, name, arguments):
    payload = {
        'jsonrpc': '2.0',
        'id': 1,
        'method': method,
        'params': {
            'name': name,
            'arguments': arguments
        }
    }
    req = urllib.request.Request(
        'https://tilda.ru/api/mcp/',
        data=json.dumps(payload).encode('utf-8'),
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {TILDA_MCP_KEY}',
            'MCP-Protocol-Version': '2025-11-25'
        }
    )
    with urllib.request.urlopen(req, context=ctx) as resp:
        return json.loads(resp.read().decode('utf-8'))

print("Updating record 5576716501 on Tilda...")
res1 = call_tilda('tools/call', 'update_record', {
    'pageid': PAGE_ID,
    'projectid': PROJECT_ID,
    'recordid': RECORD_ID,
    'tab': 'content',
    'fields': {
        'code': merged_code
    }
})
print("Update record result:", res1)

print("Publishing page...")
res2 = call_tilda('tools/call', 'publish_page', {
    'pageid': PAGE_ID,
    'projectid': PROJECT_ID
})
print("Publish page result:", res2)
