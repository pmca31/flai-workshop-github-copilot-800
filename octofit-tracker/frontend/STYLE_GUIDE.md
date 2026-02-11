# OctoFit Tracker - Style Guide

## 🎨 Color Palette

### Primary Colors
- **Primary Purple**: `#667eea` → `#764ba2` (Gradient)
- **Navy Blue**: `#1e3c72` → `#2a5298` (Navbar gradient)
- **Accent Gold**: `#ffd700` (Hover states)

### Secondary Colors
- **Success Green**: `#56ab2f` → `#a8e063` (Gradient)
- **Info Blue**: `#4facfe` → `#00f2fe` (Gradient)
- **Warning Pink**: `#f093fb` → `#f5576c` (Gradient)
- **Danger Red**: `#ff6b6b` → `#ee5a6f` (Gradient)
- **Secondary Gray**: `#6c757d` → `#5a6268` (Gradient)

### Text Colors
- **Heading Dark**: `#2c3e50`
- **Navy Text**: `#1e3c72`
- **Body Text**: `#444`

### Background
- **App Background**: Purple gradient `#667eea` → `#764ba2` (fixed to viewport)
- **Container Background**: `#ffffff` with shadow and rounded corners
- **Table Hover**: Semi-transparent purple gradient overlay

## 🖼️ Logo & Branding

### Logo Files
- **Location**: `docs/octofitapp-small.png`
- **Navbar**: 40px height, left-aligned with brand text
- **Favicon**: Referenced in HTML head
- **Manifest**: Multiple sizes for PWA support

### Logo Integration
```html
<img 
  src="%PUBLIC_URL%/octofitapp-small.png" 
  alt="OctoFit Logo" 
  height="40" 
  className="me-2"
/>
```

## 📐 Components Styling

### Navbar
- **Background**: Navy blue gradient `#1e3c72` → `#2a5298`
- **Logo**: 40px height, rotates on hover
- **Links**: White text, gold hover with gradient background
- **Shadow**: 8px with 20% opacity

### Tables
- **Header**: Navy gradient with white bold text
- **Rows**: Hover effect with purple gradient overlay and slide animation
- **Shadow**: 12px blur with 10% opacity
- **Border**: Rounded 8px corners

### Buttons
- **Primary**: Purple gradient with shadow
- **Success**: Green gradient
- **Danger**: Red gradient
- **Outline**: 2px border, fills on hover
- **Size Large**: 1rem padding, 1.1rem font

### Cards
- **Border**: None (shadow only)
- **Header**: Gradient background with white text
- **Body**: 1.5rem padding
- **Hover**: Lifts 5px with enhanced shadow

### Badges
- **Style**: Rounded 20px, bold 700 weight
- **Shadow**: Color-matched 8px blur
- **Padding**: 0.5rem × 0.75rem

## ✨ Animations & Effects

### Transitions
- All interactive elements: `0.3s ease`
- Smooth color changes, transforms, and shadows

### Hover Effects
- **Logo**: Rotate 5° and scale 1.1
- **Navbar Links**: Slide up 2px with gold glow
- **Table Rows**: Slide right 5px with purple glow
- **Buttons**: Lift 3px with enhanced shadow
- **Cards**: Lift 5px with enhanced shadow

### Keyframe Animations
- **Fade In**: Container entrance (0.5s)
- **Pulse**: Welcome heading (2s infinite)

## 📱 Responsive Design

### Breakpoints
- **Mobile** (< 768px):
  - Smaller navbar brand (1.2rem)
  - Reduced container padding (1rem)
  - Smaller welcome heading (2rem)
  - Reduced table font (0.9rem)

### Mobile Optimizations
- Collapsible navigation menu
- Stacked card layouts
- Scrollable tables (table-responsive)
- Touch-friendly button sizes

## 🎯 Typography

### Font Weights
- **Bold**: 700 (headings, buttons, badges)
- **Semi-Bold**: 600 (table headers)
- **Medium**: 500 (body text, nav links)

### Font Sizes
- **H1**: 3.5rem (mobile: 2rem)
- **H2-H6**: Varies with text-shadow
- **Lead Text**: 1.3rem
- **Body**: Default Bootstrap
- **Small**: 0.85rem (badges, meta)

### Text Effects
- **Headings**: 1px shadow for depth
- **H1**: Gradient text (webkit-text-fill-color)
- **H2**: Gradient border-bottom

## 🔧 Usage Examples

### Creating a Styled Table
```jsx
<div className="table-responsive">
  <table className="table table-hover">
    <thead>
      <tr>
        <th>Column 1</th>
        <th>Column 2</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Data 1</td>
        <td>Data 2</td>
      </tr>
    </tbody>
  </table>
</div>
```

### Creating Styled Buttons
```jsx
<button className="btn btn-primary">Primary Action</button>
<button className="btn btn-success btn-lg">Large Success</button>
<button className="btn btn-outline-primary">Outline</button>
```

### Creating Badges
```jsx
<span className="badge bg-primary">Primary</span>
<span className="badge bg-success">Success</span>
<span className="badge bg-warning text-dark">Warning</span>
```

### Loading Spinner
```jsx
<div className="loading-spinner">
  <div className="spinner-border text-primary" role="status">
    <span className="visually-hidden">Loading...</span>
  </div>
</div>
```

## 🎨 Design Principles

1. **Consistency**: All gradients flow the same direction (135deg)
2. **Depth**: Layered shadows create visual hierarchy
3. **Animation**: Smooth transitions enhance user experience
4. **Color**: Vibrant gradients with professional navy accents
5. **Accessibility**: High contrast text, visible focus states
6. **Responsiveness**: Mobile-first approach with breakpoints

## 🚀 Implementation Checklist

- ✅ App.css with complete color system
- ✅ Logo integrated in navbar (left-aligned)
- ✅ Favicon configured (octofitapp-small.png)
- ✅ Manifest.json updated with branding
- ✅ All components use Bootstrap tables
- ✅ Consistent button styling across app
- ✅ Gradient backgrounds and effects
- ✅ Hover animations on all interactive elements
- ✅ Responsive design for mobile devices
- ✅ Loading spinners and error states

## 📦 Files Modified

1. `src/App.css` - Complete style system
2. `src/App.js` - Logo in navbar
3. `public/index.html` - Title and favicon
4. `public/manifest.json` - PWA configuration
5. `setup.sh` - Automated logo copying
6. All component files - Bootstrap tables and styling

---

**OctoFit Tracker** - Modern, responsive, and beautifully styled fitness tracking application! 💪✨
