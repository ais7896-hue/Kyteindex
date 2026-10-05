/**
 * assets/i18n.js
 * Kyte Suite 官網中英文多語言字典與動態切換引擎
 */

const TRANSLATIONS = {
    zh_TW: {
        "page.title": "Kyte Suite - 為 Windows 打造的次世代桌面旗艦效率生態系 | KyteView · KyteShelf · KyteRename",
        "top.announcement_badge": "Kyte Suite 2026",
        "top.announcement_text": "Windows 次世代旗艦三部曲全線就緒：KyteView v1.5.0 · KyteShelf v1.4.0 · KyteRename v1.1.0",
        
        "nav.suite": "生態三部曲",
        "nav.workflow": "黃金工作流",
        "nav.matrix": "規格對照",
        "nav.downloads": "下載中心",
        "nav.faq": "常見問答",
        "nav.all_downloads": "全系列下載",

        "hero.badge": "專為 Windows 10 / 11 深度雕琢的現代桌面效率生態系",
        "hero.title_pre": "預覽 · 暫存 · 更名",
        "hero.title_post": "Windows 桌面生產力三部曲",
        "hero.desc": "告別繁瑣的操作摩擦與雜亂工作流！Kyte Suite 整合三大核心桌面工具：按一下空白鍵瞬開預覽的 <strong class='text-indigo-400'>KyteView</strong>、晃動滑鼠即刻吸附的 <strong class='text-sky-400'>KyteShelf</strong>、以及 50ms 零延遲拓撲更名的 <strong class='text-blue-400'>KyteRename</strong>。純本機運作、極速直覺、零雲端隱私疑慮。",
        "hero.btn_explore": "探索三大核心產品",
        "hero.btn_hub": "一站式下載中心",

        "mini.view_title": "KyteView",
        "mini.view_tag": "檔案即時預覽神器",
        "mini.view_desc": "按一下 Space 空白鍵，內容瞬間彈出！支援 Office 簡報、4K 影音硬解、壓縮檔單檔拖曳抽出與程式碼語法高亮。",
        "mini.view_feature": "50ms 瞬開 · 智慧避讓",
        "mini.official": "官網",

        "mini.shelf_title": "KyteShelf",
        "mini.shelf_tag": "桌面懸浮暫存置物架",
        "mini.shelf_desc": "按住檔案晃動滑鼠，置物架立即召喚！支援剪貼簿智慧貼入、大圖懸停預覽、一鍵打包 ZIP 與 Outlook 郵件直接附加。",
        "mini.shelf_feature": "晃動召喚 · 跨視窗中轉",

        "mini.rename_title": "KyteRename",
        "mini.rename_tag": "智慧批次重新命名",
        "mini.rename_desc": "雙欄 50ms 零延遲對照！琥珀金正則高亮、相片 EXIF/音樂 ID3 抽取、三階段安全 DAG 拓撲換名與 Ctrl+Z 快照安全還原。",
        "mini.rename_feature": "雙欄即時預覽 · 拓撲安全",

        "showcase.badge": "Product Showcase",
        "showcase.title": "三大旗艦產品 深度解析",
        "showcase.desc": "每一款軟體均為獨立專業利器，組合在一起更發揮一加一大於二的協同效應。",

        "view.part": "PART 01 · 快速檢視與內容確認",
        "view.name": "KyteView",
        "view.tagline": "次世代 Windows 極速檔案預覽神器",
        "view.desc": "不再為了確認一份 PPTX 簡報或 4K 影音反覆開啟臃腫的 Office 或外掛播放器。選中檔案按一下 <kbd class='px-2 py-0.5 rounded bg-slate-800 border border-slate-700 font-mono-code text-indigo-300 font-bold text-xs'>Space</kbd> 空白鍵，內容瞬間秒開。具備 Windows 11 原生 Mica 毛玻璃材質、智慧避讓偏移與側邊釘選模式。",
        "view.feat1": "Office 免裝本體秒開",
        "view.feat2": "壓縮檔單檔直接拖曳抽出",
        "view.feat3": "GPU 4K 硬解影音播放",
        "view.feat4": "智慧避讓與 8 向邊緣縮放",
        "view.btn_site": "進入 KyteView 官方首頁",
        "view.btn_guide": "操作指南",
        "view.btn_installer": "下載安裝版 (v1.5.0)",
        "view.btn_portable": "免安裝綠色版",

        "shelf.part": "PART 02 · 收集暫存與多向中轉",
        "shelf.name": "KyteShelf",
        "shelf.tagline": "桌面懸浮拖曳暫存置物架",
        "shelf.desc": "在 Windows 上跨資料夾、跨應用程式移動檔案時不再手忙腳亂。當你抓住檔案並輕微左右晃動滑鼠，置物架便會自動浮現在游標手邊，讓你隨手暫存檔案，支援多次收集後一口氣拖入目的地。",
        "shelf.feat1": "晃動即召喚 (Shake to Summon)",
        "shelf.feat2": "剪貼簿文字/圖片快速貼入",
        "shelf.feat3": "Outlook 郵件附件一鍵掛載",
        "shelf.feat4": "一鍵打包壓縮為 ZIP",
        "shelf.btn_site": "進入 KyteShelf 官方首頁",
        "shelf.btn_guide": "操作指南",
        "shelf.btn_installer": "下載安裝版 (v1.4.0)",
        "shelf.btn_portable": "免安裝綠色版",

        "rename.part": "PART 03 · 智慧重構與拓撲改名",
        "rename.name": "KyteRename",
        "rename.tagline": "次世代智慧批次重新命名神器",
        "rename.desc": "結合萬級檔案虛擬滾動、琥珀金正則高亮匹配、相片 EXIF/音樂 ID3 深度抽取與三階段 DAG 拓撲改名技術。解決循環改名相撞問題，每次更名自動記錄原子快照日誌，隨時按 <kbd class='px-2 py-0.5 rounded bg-slate-800 border border-slate-700 font-mono-code text-blue-300 font-bold text-xs'>Ctrl+Z</kbd> 毫秒級安全原路還原。",
        "rename.feat1": "琥珀金動態高亮匹配",
        "rename.feat2": "三階段 DAG 拓撲換名",
        "rename.feat3": "相片 EXIF & 音樂 ID3 抽取",
        "rename.feat4": "Ctrl+Z 快照安全原子還原",
        "rename.btn_site": "進入 KyteRename 官方首頁",
        "rename.btn_guide": "操作指南",
        "rename.btn_installer": "下載安裝版 (v1.1.0)",
        "rename.btn_portable": "免安裝綠色版",

        "workflow.badge": "Seamless Synergy",
        "workflow.title": "三位一體：無縫串聯的桌面工作流",
        "workflow.desc": "見證 Kyte Suite 如何將散落的日常動作轉化為流暢無阻的優雅節奏。",
        "workflow.step1_title": "KyteShelf：晃動收集暫存",
        "workflow.step1_desc": "在網頁下載圖片、從通訊軟體接收文件，或是跨資料夾翻找素材時，抓住檔案左右晃動游標，KyteShelf 置物架自動彈出接收，一次打包多來源資產。",
        "workflow.step2_title": "KyteView：空白鍵毫秒檢驗",
        "workflow.step2_desc": "在檔案清單或暫存架中，按一下 <kbd class='px-1.5 py-0.5 rounded bg-slate-800 text-indigo-300 font-mono-code text-xs'>Space</kbd> 空白鍵，直接預覽相片解析度、簡報投影片與影音內容，無需開啟肥大主程式即可迅速確認。",
        "workflow.step3_title": "KyteRename：拓撲改名安全歸檔",
        "workflow.step3_desc": "將收集好的檔案拖入 KyteRename，自動套用 EXIF 拍攝時間、音樂 ID3 標籤與智慧流水號，雙欄即時對照無誤後，透過 DAG 拓撲引擎一秒安全提交更名歸檔。",

        "matrix.badge": "Technical Specifications",
        "matrix.title": "Kyte Suite 全系列規格對照",
        "matrix.desc": "秉持極致輕量、純本機運作、無廣告、無隱私上傳的設計哲學。",
        "matrix.col_metric": "產品與指標",
        "matrix.col_view": "KyteView (預覽)",
        "matrix.col_shelf": "KyteShelf (暫存)",
        "matrix.col_rename": "KyteRename (更名)",
        "matrix.r1_metric": "主要功能定位",
        "matrix.r1_view": "Space 快速預覽 Office/影音/壓縮包",
        "matrix.r1_shelf": "晃動召喚桌面懸浮暫存中轉架",
        "matrix.r1_rename": "雙欄 50ms 零延遲安全拓撲批次改名",
        "matrix.r2_metric": "啟動快捷操作",
        "matrix.r2_view": "Space / ESC",
        "matrix.r2_shelf": "滑鼠晃動 / Ctrl + ~",
        "matrix.r2_rename": "桌面圖示 / 右鍵選單",
        "matrix.r3_metric": "系統相容性",
        "matrix.r3_all": "Windows 10 / 11 (64-bit)",
        "matrix.r4_metric": "資料隱私安全性",
        "matrix.r4_view": "100% 本地端離線解析",
        "matrix.r4_shelf": "純本機暫存，無雲端依賴",
        "matrix.r4_rename": "本地原子快照，支援 Ctrl+Z 還原",
        "matrix.r5_metric": "跨軟體生態協同",
        "matrix.r5_view": "支援 KyteRename 管道通訊",
        "matrix.r5_shelf": "支援全視窗拖放與 Outlook 附加",
        "matrix.r5_rename": "內建 Space 鍵連動 KyteView 預覽",

        "downloads.badge": "Download Hub",
        "downloads.title": "一站式全系列下載中心",
        "downloads.desc": "全部工具均經過 Windows 10/11 嚴格編譯測試，支援乾淨卸載、純綠色便攜或標準安裝精靈。",
        "downloads.stable": "穩定版",
        "downloads.installer": "下載 Windows 安裝版",
        "downloads.portable": "下載免安裝綠色版 (Portable .zip)",
        "downloads.site": "產品官網",
        "downloads.guide": "操作指南",
        "downloads.view_desc": "Windows 空白鍵快速預覽。免開 Office 預覽、4K 影音預播、隨選文字抽取。",
        "downloads.shelf_desc": "桌面隨手吸附暫存置物架。晃動滑鼠立即浮現暫存、剪貼簿一鍵貼上、ZIP 壓縮包、Outlook 快捷拖曳。",
        "downloads.rename_desc": "新一代智慧批次更名。超 50ms 極速雙欄即時對照、琥珀金正則、EXIF/ID3、拓撲安全 DAG 循環破圈改名。",

        "faq.badge": "Questions & Answers",
        "faq.title": "常見問與答",
        "faq.q1": "三款軟體是強制綁定還是可以各自獨立單獨使用？",
        "faq.a1": "完全可以各自獨立單獨使用！KyteView、KyteShelf 與 KyteRename 均為獨立免依賴的 Windows 應用程式。當您同時安裝兩款以上時，程式會自動透過 Windows Named Pipe IPC 啟動雙向無縫協同功能（例如在 KyteRename 清單按 Space 喚起 KyteView 預覽）。",
        "faq.q2": "這些軟體是否會收集或上傳我的本機個人檔案？",
        "faq.a2": "絕對不會！Kyte Suite 全系列產品均為 100% 本機純離線運作工具。所有的預覽渲染、中繼資料抽取、暫存與重新命名作業均在您本機電腦的記憶體與 CPU/GPU 內完成，絕不連網傳輸您的任何檔案內容，隱私絕對安全。",
        "faq.q3": "如果公司電腦沒有管理員權限，可以使用綠色免安裝版嗎？",
        "faq.a3": "可以！各產品在官方發行頁面除了提供標準 Inno Setup 安裝檔之外，亦提供便攜免安裝綠色壓縮包，解壓縮後直接雙擊執行即可使用，無需管理員提權。",

        "footer.slogan": "The Modern Windows Productivity Ecosystem",
        "footer.rights": "© 2026 ais7896-hue. All rights reserved. Designed with precision for Windows 10 & 11.",
        "footer.privacy": "純本機離線安全 · 零隱私收集 · 極致效能",
        "footer.view_site": "KyteView 官網",
        "footer.shelf_site": "KyteShelf 官網",
        "footer.rename_site": "KyteRename 官網",
        "footer.support": "支援信箱",
    },

    en_US: {
        "page.title": "Kyte Suite - The Next-Gen Windows Desktop Productivity Ecosystem | KyteView · KyteShelf · KyteRename",
        "top.announcement_badge": "Kyte Suite 2026",
        "top.announcement_text": "The Next-Gen Windows Productivity Trio is Ready: KyteView v1.5.0 · KyteShelf v1.4.0 · KyteRename v1.1.0",
        
        "nav.suite": "The Trio",
        "nav.workflow": "Workflow",
        "nav.matrix": "Specifications",
        "nav.downloads": "Downloads",
        "nav.faq": "FAQ",
        "nav.all_downloads": "Download All",

        "hero.badge": "Crafted Exclusively for Windows 10 & 11 Desktop Productivity",
        "hero.title_pre": "Preview · Stash · Rename",
        "hero.title_post": "The Ultimate Windows Desktop Productivity Trio",
        "hero.desc": "Say goodbye to desktop friction! Kyte Suite unifies three essential tools: <strong class='text-indigo-400'>KyteView</strong> for lightning-fast spacebar previews, <strong class='text-sky-400'>KyteShelf</strong> for intuitive shake-to-summon file stashing, and <strong class='text-blue-400'>KyteRename</strong> for zero-latency topological safe batch renaming. 100% local, instant, and zero cloud dependency.",
        "hero.btn_explore": "Explore the Ecosystem",
        "hero.btn_hub": "Download Hub",

        "mini.view_title": "KyteView",
        "mini.view_tag": "Instant Spacebar Preview Tool",
        "mini.view_desc": "Press Spacebar to peek inside files instantly! Supports Office docs, 4K hardware-accelerated video, single-file archive extraction, and code syntax highlighting.",
        "mini.view_feature": "50ms Instant Pop · Smart Offsetting",
        "mini.official": "Website",

        "mini.shelf_title": "KyteShelf",
        "mini.shelf_tag": "Floating Desktop Staging Shelf",
        "mini.shelf_desc": "Shake your mouse while dragging files to summon the floating shelf! Smart clipboard paste, hover thumbnail zoom, one-click ZIP packaging, and Outlook drop.",
        "mini.shelf_feature": "Shake to Summon · Multi-window Relay",

        "mini.rename_title": "KyteRename",
        "mini.rename_tag": "Smart Batch Renaming",
        "mini.rename_desc": "Dual-pane 50ms zero-latency preview! Amber regex highlight, photo EXIF / music ID3 extraction, 3-phase cycle-free DAG engine, and Ctrl+Z undo.",
        "mini.rename_feature": "Live Dual-Pane · Topological Safety",

        "showcase.badge": "Product Showcase",
        "showcase.title": "Deep Dive: The Three Pillars",
        "showcase.desc": "Each application is a standalone, powerhouse utility, combining together to unlock a multiplier in daily workflow efficiency.",

        "view.part": "PART 01 · Instant Inspection & Content Verification",
        "view.name": "KyteView",
        "view.tagline": "Next-Gen Lightning Spacebar File Preview for Windows",
        "view.desc": "No need to wait for heavy desktop suites just to check a slide or video. Press <kbd class='px-2 py-0.5 rounded bg-slate-800 border border-slate-700 font-mono-code text-indigo-300 font-bold text-xs'>Space</kbd> on any file to inspect immediately. Features native Windows 11 Mica material, smart collision dodging, and split-dock pinning.",
        "view.feat1": "Open Office docs without Office installed",
        "view.feat2": "Drag single files out of archives directly",
        "view.feat3": "GPU-accelerated 4K video playback",
        "view.feat4": "Smart offsetting & 8-direction edge resize",
        "view.btn_site": "Visit KyteView Website",
        "view.btn_guide": "User Guide",
        "view.btn_installer": "Download Installer (v1.5.0)",
        "view.btn_portable": "Portable .zip",

        "shelf.part": "PART 02 · Stash, Collect & Multi-target Relay",
        "shelf.name": "KyteShelf",
        "shelf.tagline": "Desktop Floating Drag & Drop Staging Shelf",
        "shelf.desc": "Eliminate window toggling friction. Whenever you drag a file and shake your mouse slightly, KyteShelf summons instantly beside your cursor to hold files temporarily until you are ready to drop them.",
        "shelf.feat1": "Shake to Summon (Shake gesture detection)",
        "shelf.feat2": "Smart clipboard text / image paste",
        "shelf.feat3": "Direct drop into Outlook email attachments",
        "shelf.feat4": "One-click ZIP archive packaging",
        "shelf.btn_site": "Visit KyteShelf Website",
        "shelf.btn_guide": "User Guide",
        "shelf.btn_installer": "Download Installer (v1.4.0)",
        "shelf.btn_portable": "Portable .zip",

        "rename.part": "PART 03 · Smart Restructuring & Topological Renaming",
        "rename.name": "KyteRename",
        "rename.tagline": "Next-Gen Batch Renaming with Real-Time Safety",
        "rename.desc": "Engineered with virtual scrolling for 10,000+ files, amber regex token highlighting, deep EXIF / ID3 extraction, and a 3-phase DAG renaming engine. Resolves cyclic collision conflicts, backed by millisecond-level <kbd class='px-2 py-0.5 rounded bg-slate-800 border border-slate-700 font-mono-code text-blue-300 font-bold text-xs'>Ctrl+Z</kbd> atomic undo.",
        "rename.feat1": "Dynamic amber regex token highlighting",
        "rename.feat2": "3-phase DAG cyclic collision resolver",
        "rename.feat3": "Photo EXIF & audio ID3 tag extraction",
        "rename.feat4": "Ctrl+Z atomic snapshot rollback",
        "rename.btn_site": "Visit KyteRename Website",
        "rename.btn_guide": "User Guide",
        "rename.btn_installer": "Download Installer (v1.1.0)",
        "rename.btn_portable": "Portable .zip",

        "workflow.badge": "Seamless Synergy",
        "workflow.title": "Triad Harmony: The Frictionless Desktop Flow",
        "workflow.desc": "Witness how Kyte Suite transforms chaotic everyday desktop interactions into effortless precision.",
        "workflow.step1_title": "KyteShelf: Shake & Collect",
        "workflow.step1_desc": "Download assets from browser or chat apps, shake the mouse cursor to summon KyteShelf, and stage files from scattered sources into one temporary tray.",
        "workflow.step2_title": "KyteView: Millisecond Inspection",
        "workflow.step2_desc": "Hover on any file inside Explorer or KyteShelf, tap <kbd class='px-1.5 py-0.5 rounded bg-slate-800 text-indigo-300 font-mono-code text-xs'>Space</kbd> to inspect high-res photos, slides, or media clips without launching heavy software.",
        "workflow.step3_title": "KyteRename: Safe Topological Archiving",
        "workflow.step3_desc": "Drag staged files directly into KyteRename. Apply EXIF timestamps, ID3 tags, and smart numbering. Preview results in real-time, then commit with zero collision risk.",

        "matrix.badge": "Technical Specifications",
        "matrix.title": "Kyte Suite Comprehensive Comparison",
        "matrix.desc": "Built with the philosophy of ultra-lightweight performance, 100% local processing, zero ads, and zero telemetry.",
        "matrix.col_metric": "Specs & Capabilities",
        "matrix.col_view": "KyteView (Preview)",
        "matrix.col_shelf": "KyteShelf (Staging)",
        "matrix.col_rename": "KyteRename (Rename)",
        "matrix.r1_metric": "Core Purpose",
        "matrix.r1_view": "Spacebar preview for Office, Media & Archives",
        "matrix.r1_shelf": "Shake-summon floating desktop staging shelf",
        "matrix.r1_rename": "Dual-pane 50ms zero-latency safe batch renaming",
        "matrix.r2_metric": "Primary Shortcut",
        "matrix.r2_view": "Space / ESC",
        "matrix.r2_shelf": "Mouse Shake / Ctrl + ~",
        "matrix.r2_rename": "Desktop Shortcut / Context Menu",
        "matrix.r3_metric": "System Compatibility",
        "matrix.r3_all": "Windows 10 / 11 (64-bit)",
        "matrix.r4_metric": "Privacy & Security",
        "matrix.r4_view": "100% Local offline parsing",
        "matrix.r4_shelf": "Local RAM/disk buffer, zero cloud sync",
        "matrix.r4_rename": "Atomic local journal, Ctrl+Z reversible",
        "matrix.r5_metric": "Inter-App Synergy",
        "matrix.r5_view": "Supports IPC with KyteRename",
        "matrix.r5_shelf": "Universal drag-and-drop & Outlook attachments",
        "matrix.r5_rename": "Native Space key preview via KyteView",

        "downloads.badge": "Download Hub",
        "downloads.title": "Unified Download Center",
        "downloads.desc": "All utilities are compiled, signed, and tested on Windows 10/11. Supports clean uninstaller, standard setup, and portable zero-install zip archives.",
        "downloads.stable": "Stable Release",
        "downloads.installer": "Download Windows Setup",
        "downloads.portable": "Download Portable (.zip)",
        "downloads.site": "Website",
        "downloads.guide": "User Guide",
        "downloads.view_desc": "Windows spacebar fast preview. Peek Office docs, 4K video playback, and selective text extraction.",
        "downloads.shelf_desc": "Desktop floating staging shelf. Shake mouse to summon, clipboard paste, zip bundle, and Outlook drop.",
        "downloads.rename_desc": "Next-gen batch renaming. 50ms live dual-pane preview, regex highlight, EXIF/ID3, and DAG cycle-free engine.",

        "faq.badge": "Questions & Answers",
        "faq.title": "Frequently Asked Questions",
        "faq.q1": "Are the apps bundled or can they be used independently?",
        "faq.a1": "Each app is 100% standalone! KyteView, KyteShelf, and KyteRename do not depend on each other. However, when multiple apps are installed, they automatically discover each other via Windows Named Pipe IPC to unlock cross-app synergy (e.g. pressing Space in KyteRename triggers KyteView).",
        "faq.q2": "Do these applications upload or collect my files?",
        "faq.a2": "Never! All Kyte Suite products run 100% offline on your local machine. All previewing, metadata extraction, staging, and renaming operations take place strictly within your local CPU/GPU and RAM. No telemetry or file data is ever transmitted over the network.",
        "faq.q3": "Can I use the portable edition without administrator privileges?",
        "faq.a3": "Yes! In addition to standard Inno Setup wizards, all applications provide portable zero-install ZIP packages. Simply extract and double-click to run without requiring admin elevation.",

        "footer.slogan": "The Modern Windows Productivity Ecosystem",
        "footer.rights": "© 2026 ais7896-hue. All rights reserved. Designed with precision for Windows 10 & 11.",
        "footer.privacy": "100% Local & Offline · Zero Telemetry · Extreme Performance",
        "footer.view_site": "KyteView",
        "footer.shelf_site": "KyteShelf",
        "footer.rename_site": "KyteRename",
        "footer.support": "Support Email",
    }
};

let currentLang = 'zh_TW';

function getInitialLanguage() {
    const saved = localStorage.getItem('kyte_suite_lang');
    if (saved && (saved === 'zh_TW' || saved === 'en_US')) {
        return saved;
    }
    const sysLang = navigator.language || navigator.userLanguage || '';
    if (sysLang.toLowerCase().includes('zh')) {
        return 'zh_TW';
    }
    return 'en_US';
}

function applyLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('kyte_suite_lang', lang);
    document.documentElement.lang = lang === 'zh_TW' ? 'zh-TW' : 'en';

    const dict = TRANSLATIONS[lang] || TRANSLATIONS.zh_TW;

    if (dict["page.title"]) {
        document.title = dict["page.title"];
    }

    const elements = document.querySelectorAll('[data-i18n]');
    elements.forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key]) {
            el.innerHTML = dict[key];
        }
    });

    const langBtnText = document.getElementById('lang-btn-text');
    if (langBtnText) {
        langBtnText.textContent = lang === 'zh_TW' ? 'EN' : '繁中';
    }
}

function toggleLanguage() {
    const nextLang = currentLang === 'zh_TW' ? 'en_US' : 'zh_TW';
    applyLanguage(nextLang);
}

document.addEventListener('DOMContentLoaded', () => {
    const initial = getInitialLanguage();
    applyLanguage(initial);

    const toggleBtn = document.getElementById('lang-toggle-btn');
    if (toggleBtn) {
        toggleBtn.addEventListener('click', toggleLanguage);
    }
});
