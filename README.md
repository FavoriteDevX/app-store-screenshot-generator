# 📱 Automated App Store Screenshot Generator

<img width="800" height="311" alt="image" src="https://github.com/user-attachments/assets/dc568aef-cd23-4d29-a059-f4a516f2218a" />

> A production-grade Python automation CLI engine designed for Apple App Store designers and indie developers to programmatically batch-process raw interface viewports into standardized, localized, presentation-ready marketing assets.

## 💎 Structural Engine Powers
*   **Multi-Device Resolution Scaling:** Automatically maps input layouts to match specific Apple submission requirements (6.7" iPhone Display up to 12.9" iPad Pro matrices).
*   **Dynamic Layout Centering:** Scales screenshot assets using Lanczos downsampling routines and centers coordinates symmetrically while protecting safety padding margins.
*   **Zero Graphic Tool Dependencies:** Operates completely via the headless Python Imaging Library, running seamlessly inside GitHub Actions CI/CD automation pipelines.

## 🚀 Execution Guide
Ensure dependencies are satisfied:
```bash
pip install -r requirements.txt
```

Run the generator payload mapping your text overlay declarations:
```bash
python generator.py "Track Your Metrics\n100% Offline, Securely"
```
