# SketchUp Plugins για Αρχιτεκτονικό Γραφείο — Τεκμηριωμένη Βάση Γνώσης (2026)

> Πηγή τροφοδοσίας για NotebookLM. Όλα τα στοιχεία είναι διασταυρωμένα από επίσημες πηγές
> (Extension Warehouse, help.sketchup.com, ιστοσελίδες developer, SketchUcation, Chaos, D5)
> τον Ιούνιο 2026. Όπου ένα στοιχείο δεν επιβεβαιώθηκε πλήρως, σημειώνεται ρητά ως
> «ΠΡΟΣ ΕΠΑΛΗΘΕΥΣΗ». Οι τιμές αλλάζουν — επιβεβαιώστε live πριν από αγορά.

---

## 0. Η κεντρική φιλοσοφία (το πιο σημαντικό μήνυμα)

Η σειρά είναι: **πρώτα σταθερότητα/υγιεινή → μετά ταχύτητα → μετά οπτικοποίηση.**

Το πιο συχνό λάθος ενός γραφείου είναι να εγκαταστήσει 20–30 plugins την πρώτη μέρα.
Αποτέλεσμα: file bloat, conflicts, crashes, και μοντέλα που κανείς άλλος δεν μπορεί να
επεξεργαστεί. Διδάσκουμε **λίγα, επαληθευμένα εργαλεία**, με πρακτική άσκηση πάνω σε
πραγματικό αρχείο γραφείου — όχι λίστα 40 plugins.

Το σύγχρονο native SketchUp (2024–2026) είναι ήδη πολύ ικανό. Βάζουμε plugin **μόνο εκεί
που η native γεωμετρία αποτυγχάνει ή είναι πολύ αργή**.

---

## 1. Επίσημο πλαίσιο SketchUp 2026

- **Υποστηριζόμενες εκδόσεις:** 2024, 2025, 2026. Η 2023 αποσύρθηκε (End of Support 31 Ιαν 2026).
  Πολιτική: η υποστήριξη λήγει 31 Ιανουαρίου, τρία χρόνια μετά το έτος κυκλοφορίας.
  *(help.sketchup.com — Supported Versions / End of Support Policy)*
- **Νέα μηχανή γραφικών (από 2024):** δίνει PBR υλικά, ambient occlusion, image-based lighting.
  Απαιτεί **DirectX 12 (feature-level 11.0) σε Windows** ή **Metal 2 σε macOS**. Αν δεν πληρούνται,
  πέφτει στο «Classic graphics». *(help.sketchup.com — System Requirements)*
- **GPU/VRAM:** Συνιστάται **dedicated GPU**. Πρακτικά 6–8 GB VRAM καλύπτουν τα περισσότερα
  επαγγελματικά μοντέλα· για βαριά PBR/AO/IBL η επίσημη καθοδήγηση δείχνει πολύ υψηλότερη VRAM
  (16 GB, ιδανικά 32 GB σε ακραία PBR-heavy μοντέλα). *(Το ακριβές «8GB» wording: ΠΡΟΣ ΕΠΑΛΗΘΕΥΣΗ στη live σελίδα.)*
- **Pro vs Studio:**
  - **SketchUp Pro** (~$399/έτος): core modeling, LayOut, extensions. Windows + Mac.
  - **SketchUp Studio** (~$819/έτος): ό,τι έχει το Pro **+ V-Ray + Scan Essentials + environments**.
    **Studio = μόνο Windows.** Σε Mac δεν παίρνεις το ενσωματωμένο V-Ray/Scan Essentials.
- **Native εργαλεία που «διπλασιάζουν» plugins (μην βάζετε περιττά):**
  - **Solid Tools** (Union, Subtract, Trim, Intersect, Split, Outer Shell) — boolean operations.
  - **Sandbox Tools** — terrain/TIN (From Contours, From Scratch, Smoove, Stamp, Drape, Add Detail).
  - **Native Section Fills** — γεμισμένες τομές, native από SketchUp 2024.
  - **Overlays** — framework από SketchUp 2023 για live πληροφορία στο viewport.

---

## 2. Υγιεινή μοντέλου — ThomThom (ΟΛΑ ΔΩΡΕΑΝ, MIT) — το «Day 1» πακέτο

### TT_Lib² (TT_Lib2)
- Δωρεάν βιβλιοθήκη (όχι εργαλείο με UI). **Εγκαθίσταται ΠΡΩΤΗ** γιατί είναι dependency του CleanUp³.
- Συμβατή με SketchUp 2022–2026 (Win/Mac). *(Extension Warehouse listing)*
- Συχνό σφάλμα: «TT_Lib² is not installed» αν λείπει ή εγκατασταθεί μερικώς.

### CleanUp³
- Δωρεάν, open-source. Τρέχουσα έκδοση **v3.4.3**. Συμβατό 2022–2026 (Win/Mac).
- **Απαιτεί TT_Lib²** ως σκληρό dependency.
- Χρήση: purge unused, διαγραφή stray/duplicate edges & materials, merge coplanar faces, μείωση file bloat.
- Ρίσκο: το «merge coplanar» μπορεί να αλλάξει γεωμετρία — τρέξτε σε αντίγραφο με συντηρητικές ρυθμίσεις.

### Solid Inspector²
- Δωρεάν, open-source. Έκδοση **v2.5.x** (πρόσθεσε Overlays support).
- **ΔΕΝ απαιτεί TT_Lib²** (αυτόνομο — διαφορά από το CleanUp³). Μόνο η παλιά v1.x απαιτούσε TT_Lib2.
- Συμβατό τουλάχιστον 2021–2025· **2026 listing: ΠΡΟΣ ΕΠΑΛΗΘΕΥΣΗ** (πολύ πιθανό ναι).
- Χρήση: εντοπίζει/διορθώνει reversed faces, internal/stray edges, holes, non-solid groups. Τρέξτε πριν από export/3D print/rendering.

**Σειρά εγκατάστασης:** TT_Lib² → CleanUp³. Το Solid Inspector² ανεξάρτητα.

---

## 3. Ταχύτητα παραγωγής — παραμετρικά (το «ROI» πακέτο)

### Profile Builder 4 (MindSight Studios) — ESSENTIAL αν υπάρχει budget
- **License:** perpetual ΚΑΙ subscription. Perpetual ποτέ δεν λήγει, με δωρεάν μελλοντικά upgrades.
  Ενδεικτική τιμή ~$119 perpetual — **ακριβής τιμή ΠΡΟΣ ΕΠΑΛΗΘΕΥΣΗ** (reseller σε σέλιγκ ~£47).
- **Συμβατότητα:** SketchUp Pro 2022, 2023, 2024, 2025, **και 2026**. Win/Mac. Ενεργά συντηρούμενο
  (v4.0.5, Ιαν 2025).
- **Χρήση:** path-based «Assemblies» (Profiles + Components) → παραμετρικοί τοίχοι πολλαπλών στρώσεων,
  κιγκλιδώματα, σοβατεπί, φράχτες, σκάλες, δοκοί. Παραμένουν editable (profile, υλικό, ύψος, διαδρομή).
- **Ρίσκο:** αν κάνεις **explode**, χάνεται η παραμετρικότητα (γίνεται απλή γεωμετρία). Όποιος ανοίγει
  το μοντέλο χωρίς PB4 βλέπει στατική γεωμετρία.

### Quantifier Pro (MindSight Studios) — USEFUL για κοστολόγηση
- Perpetual commercial ~€79. Πωλείται και σε **BIM Bundle με Profile Builder** (~25% έκπτωση).
- Χρήση: άμεσα quantity & cost takeoffs (επιφάνεια, όγκος, μήκος, βάρος, κόστος) με reports.

### Skimp (MindSight Studios) — USEFUL για βαριά assets
- Perpetual + subscription. Απαιτεί SketchUp Pro 2020+, δουλεύει ως 2026. Έκδοση v2.0.4.
- Χρήση: import + **polygon decimation** βαριών μοντέλων (GLB, glTF, FBX, OBJ, STL, SKP…). Μειώνει
  εκατομμύρια faces σε δευτερόλεπτα κρατώντας την οπτική εμφάνιση.
- **Ρίσκο:** πολύ επιθετική μείωση → καταστροφή UV/textures. Δοκιμή ανά asset.

---

## 4. Κουφώματα & ανοίγματα — FlexTools Pro (flextools.cc) — ESSENTIAL/RECOMMENDED
- **License:** **ετήσιο subscription** — **FlexPack Pro €99/έτος (~$108)**. **Όχι trial**, αλλά
  **30-day money-back guarantee**.
- **Συμβατότητα:** SketchUp 2017–2026 (Win/Mac). Πολύ ενεργό (v2.18.1, Σεπ 2025).
- **Χρήση:** δυναμικά (responsive) components — έξυπνες πόρτες, παράθυρα, panels, σκάλες. Το **WallCutter**
  κόβει αυτόματα το άνοιγμα στον τοίχο· μετακινείς το κούφωμα → μετακινείται το άνοιγμα· scale με
  διατήρηση αναλογιών πλαισίου. Περιλαμβάνει και Zapper, Cleaner, Refresh, Flip, ComponentFinder.
- **Ρίσκο:** subscription-only — αν λήξει η άδεια, σταματά η δυναμική επεξεργασία (η γεωμετρία μένει).

---

## 5. Σύνθετες επιφάνειες & οργανικά (Fredo6 + Artisan) — προχωρημένα

### Fredo6 — Joint Push Pull & Curviloft — τώρα ΠΛΗΡΩΜΕΝΑ
- **License:** perpetual, **~$12/plugin ή $40 για το bundle των 8** Fredo6. **30-day trial**, μετά
  απαιτείται **SketchUcation License (SCFLicense)**.
- **Dependency:** **LibFredo6** (δωρεάν). Εγκαθίσταται ΠΡΩΤΗ, μετά restart. JointPushPull v4.9a (Απρ 2025)
  απαιτεί **LibFredo6 ≥ 15.3**. Τρέχουσα LibFredo6 **v15.9c (~Μάιος 2026)**.
- **Συμβατότητα:** SketchUp 2017–2026.
- **Joint Push Pull:** push/pull σε πολλαπλές & καμπύλες επιφάνειες, πάχυνση, extrude-along-normals.
- **Curviloft:** loft/skinning από contours (Loft by Spline, Loft Along Path, Skin Contours).
- **Ρίσκο:** πιο συχνό failure = λάθος έκδοση LibFredo6. Paywall + license management μέσω SketchUcation.

### Artisan 2 (MindSight Studios) — ΕΝΕΡΓΟ (όχι abandoned!)
- **Προσοχή σε παλιά claims:** το «τελευταίο update ~2011» αφορά το **Artisan 1**. Υπάρχει πλήρης
  ξαναγραφή, **Artisan 2**, που υποστηρίζει σύγχρονο SketchUp.
- **License:** **$99/έτος**, 15-day trial. Νέο προϊόν, χωρίς upgrade path από v1.
- **Συμβατότητα:** SketchUp 2022–2026 (Pro 2018+ minimum)· **ακριβές «2026» tick: ΠΡΟΣ ΕΠΑΛΗΘΕΥΣΗ**.
- **Χρήση:** organic/subdivision modeling, sculpting, terrain grading. Βαρύ σε πυκνά meshes.

---

## 6. Site, entourage & υλικά

### PlaceMaker (suplacemaker.com / MindSight) — OPTIONAL (site context)
- **Μοντέλο:** (α) **Pay-As-You-Go credits** (δεν λήγουν, ~$0.15/credit) ή (β) **annual ~$109/έτος**
  (Google Earth 3D + OpenStreetMap δωρεάν, άλλα δεδομένα με έκπτωση).
- Εισάγει: αεροφωτογραφίες, terrain, editable 3D κτίρια, δρόμους, OSM & Google Earth 3D.
- Ακριβής λίστα 2026-supported versions: ΠΡΟΣ ΕΠΑΛΗΘΕΥΣΗ.

### Skatter 2 (Lindalë) — OPTIONAL (landscape/scatter)
- **Τιμή:** perpetual **€149** ή subscription **€99/έτος** (single) / €249/έτος (floating). +ΦΠΑ.
- **Συμβατότητα:** SketchUp 2024–2026 (Win/Mac). 8 GB RAM, internet.
- **Render-Only:** στέλνει τα scatter δεδομένα **απευθείας στη render engine** (V-Ray, Enscape, Thea,
  Octane κ.ά.) χωρίς να βαραίνει το SketchUp model.
- **Ρίσκο:** αν παράγεις πραγματική γεωμετρία αντί για Render-Only proxies, μεγάλα scatters (δάση, γρασίδι)
  φουσκώνουν το αρχείο και κολλάνε το SketchUp. Το Render-Only output φαίνεται μόνο σε υποστηριζόμενη engine,
  όχι στο viewport.

### Architextures (architextures.org) — USEFUL (υλικά/textures)
- **Extension δωρεάν**· textures δωρεάν για educational/personal. **Εμπορική χρήση → Pro (~£65.99/έτος)**.
  Μηνιαία τιμή: ΠΡΟΣ ΕΠΑΛΗΘΕΥΣΗ.
- **Συμβατότητα:** SketchUp 2024–2026. Ενεργό. Web-app που δημιουργεί/εισάγει seamless παραμετρικά υλικά·
  right-click «Edit with Architextures» για re-edit.
- **Ρίσκο:** το περιεχόμενο δεν επιτρέπεται εμπορικά μετά τη λήξη της συνδρομής· απαιτεί internet.

### Eneroth Auto Weld — FREE (verify)
- Δωρεάν στο Extension Warehouse. Κώδικας ενεργός, αλλά το EW compatibility flag ιστορικά καθυστερεί.
- Χρήση: αυτόματο weld edges σε καμπύλες· διορθώνει γεωμετρία σπασμένη από επαναλαμβανόμενο Follow Me.
- **Verify:** πρόσφατα threads (2024) αναφέρουν license prompt — επιβεβαιώστε αν παραμένει 100% δωρεάν.

---

## 7. Οπτικοποίηση / Rendering — διάλεξε ΕΝΑ με βάση το hardware

> Κανόνας: **rendering μάθημα χωρίς hardware check = συνταγή για crashes.** Πρώτα ελέγξτε GPU/VRAM.

### V-Ray 7 για SketchUp (Chaos) — high-end, μέσα στο Studio
- **Συμβατότητα:** SketchUp 2023–2026 (V-Ray 7 + V-Ray 6 υποστηρίζονται· V-Ray 5 discontinued).
- **Τιμή:** subscription. Solo ~$540/έτος (named), Premium ~$719/έτος (floating). *(2025 snapshots — ΠΡΟΣ ΕΠΑΛΗΘΕΥΣΗ)*
- **Hardware:** Win + Mac (V-Ray 7 πρόσθεσε Metal GPU σε Apple Silicon). GPU mode → NVIDIA RTX.
- Περιλαμβάνεται στο SketchUp **Studio** (Windows).

### Enscape 4.13+ (Chaos) — real-time, εύκολα walkthroughs
- **Συμβατότητα:** SketchUp 2023–2026 (το 2026 θέλει Enscape 4.13+, Νοε 2025).
- **Τιμή:** subscription, Solo ~$575/έτος. **Καμία δωρεάν έκδοση.** Το **ArchDesign Collection** μπαντλάρει
  Enscape + V-Ray. *(2025 snapshots — ΠΡΟΣ ΕΠΑΛΗΘΕΥΣΗ)*
- **Hardware:** min 4 GB VRAM (8 GB+ συνιστάται), RTX recommended. Win + Mac, αλλά **Mac μόνο Apple Silicon**
  (όχι Intel Mac).

### D5 Render — δωρεάν entry, αλλά Windows-only
- **Συμβατότητα:** SketchUp 2020.1–2026 (LiveSync).
- **Τιμή:** **Community = ΔΩΡΕΑΝ** αλλά **non-commercial** (μάθηση/προσωπικό). Εμπορική δουλειά → **D5 Pro
  ~$360/έτος**. *(ΠΡΟΣ ΕΠΑΛΗΘΕΥΣΗ ακριβής τιμή)*
- **Hardware:** **Windows ΜΟΝΟ** (όχι Mac). Απαιτεί ray-tracing GPU (min GTX 1060 6GB, συνιστάται RTX 3060 Ti+),
  32 GB RAM συνιστάται.
- **Σημείωση γραφείου:** το δωρεάν tier είναι non-commercial → για πληρωμένα projects χρειάζεστε Pro.

### SketchUp Diffusion / «AI Render» (ομάδα SketchUp) — γρήγορα concept visuals
- **ΔΕΝ είναι δωρεάν & ΔΕΝ είναι αυτόνομη render engine.** Απαιτεί ενεργή συνδρομή **SketchUp Go/Pro/Studio**
  + **AI credits** (5 credits/render) + **internet** (cloud-based).
- Extension για SketchUp **2024+** (native σε iPad/Web). Διαθέσιμο σε Go, Pro ΚΑΙ Studio.

| Engine | SU 2026 | Δωρεάν tier | Mac | Min/τυπικό GPU |
|---|---|---|---|---|
| V-Ray 7 | Ναι | Όχι (trial) | Ναι (Apple Silicon, Metal) | RTX για GPU mode |
| Enscape 4.13+ | Ναι | Όχι | Ναι (μόνο Apple Silicon) | 4GB min, 8GB+ RTX |
| D5 Render | Ναι | Ναι (Community, non-commercial) | Όχι (Windows only) | GTX 1060 6GB min, RTX 3060Ti+ |
| SketchUp Diffusion | Ναι (ext. 2024+) | Όχι (Go/Pro/Studio + credits) | Ναι | Cloud (χωρίς local GPU) |

---

## 8. Παγίδες & legacy — τι ΝΑ προσέξετε

- **1001bit Tools = LEGACY/stale.** Τελευταίο Pro build **v2.2, Απρ 2022** — καμία νεότερη έκδοση.
  Freeware δωρεάν, Pro ~$48. **2026 compatibility flag: ΠΡΟΣ ΕΠΑΛΗΘΕΥΣΗ** (πιθανότατα stale). Χρήσιμο
  ακόμη για γρήγορα αρχιτεκτονικά στοιχεία (σκάλες, στέγες, περσίδες) αλλά **«test before use»** —
  ΟΧΙ core εργαλείο, παράγει non-parametric γεωμετρία.
- **Fredo6 licensing:** τα tools έγιναν paid + απαιτούν SketchUcation License· αν αλλάξει σταθμός εργασίας,
  η άδεια μπορεί να «κλειδώσει». Κεντρική διαχείριση αδειών από IT.
- **Διπλασιασμός native:** μην βάζετε plugin για boolean (υπάρχουν Solid Tools), για βασικό terrain
  (Sandbox Tools), ή για γεμισμένες τομές (native Section Fills από 2024).
- **Outdated plugins:** μην κατεβάζετε rbz από ανεπίσημα blogs — μόνο Extension Warehouse / SketchUcation.
  Παλιά plugins (π.χ. Skalp last ~2017) μπορεί να μη φορτώνουν σε 2024–2026.
- **Performance-heavy:** Skatter με πραγματική γεωμετρία, Artisan σε πυκνά meshes, βαριά PBR → lag/crash.

---

## 9. Το προτεινόμενο stack & σειρά διδασκαλίας

**Minimum stack (Day 1, όλα δωρεάν):**
1. TT_Lib² (πρώτο) + CleanUp³ — υγιεινή/optimization
2. Solid Inspector² — έλεγχος γεωμετρίας

**Recommended stack (καθημερινή παραγωγή, με budget):**
3. Profile Builder 4 — παραμετρικοί τοίχοι/προφίλ/κιγκλιδώματα
4. FlexTools Pro — κουφώματα/ανοίγματα (WallCutter)
5. Ένας renderer ανάλογα με hardware: **D5** (δωρεάν, Windows) ή **Enscape** (Win/Mac) ή **V-Ray** (Studio)
6. Architextures — υλικά

**Advanced stack (visualization/landscape teams):**
7. Joint Push Pull / Curviloft — καμπύλες/σύνθετες επιφάνειες
8. Skatter 2 — βλάστηση/entourage (Render-Only)
9. PlaceMaker — site context
10. Skimp — βαριά εισαγόμενα assets
11. Quantifier Pro — μετρήσεις/κοστολόγηση
12. Artisan 2 — οργανικά/terrain

**Τι διδάσκουμε ΠΡΩΤΑ:** τη ροή **DWG → CleanUp³ → Solid Inspector² → Profile Builder 4**. Μόλις δουν
ότι ένας τοίχος 3 στρώσεων σχεδιάζεται σε δευτερόλεπτα, υιοθετούν τη νέα ροή.

**Τι ΑΠΟΦΕΥΓΟΥΜΕ στην αρχή:** πολλά rendering subscriptions μαζί, οργανικά (Artisan), βαριά scatters,
και κάθε legacy/high-dependency εργαλείο πριν κατακτηθεί ο κορμός.
