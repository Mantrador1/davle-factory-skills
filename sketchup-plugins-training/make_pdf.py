#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Παράγει το PDF handout (ελληνικά) για την εκπαίδευση SketchUp plugins.
Παρακάμπτει το σπασμένο cryptography binding με stubs, ώστε να φορτώσει το fpdf2."""
import sys, types
for m in ['cryptography','cryptography.hazmat','cryptography.hazmat.primitives',
          'cryptography.hazmat.primitives.serialization','cryptography.hazmat.primitives.ciphers',
          'cryptography.hazmat.primitives.ciphers.algorithms','cryptography.hazmat.primitives.ciphers.modes',
          'cryptography.hazmat.backends']:
    sys.modules[m] = types.ModuleType(m)
sys.modules['cryptography.hazmat.primitives.serialization'].pkcs12 = object()
sys.modules['cryptography.hazmat.backends'].default_backend = lambda: None

from fpdf import FPDF
from fpdf.fonts import FontFace

# ---- παλέτα ----
PRIMARY = (11, 79, 108)
ORANGE  = (179, 84, 30)
GREEN   = (27, 122, 61)
RED     = (192, 57, 43)
GREY    = (90, 90, 90)
LIGHT   = (238, 245, 248)
ROW     = (245, 248, 250)
WARNBG  = (253, 243, 242)
OKBG    = (240, 248, 242)
BORDER  = (207, 216, 220)
DARK    = (26, 26, 26)

FREG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FBLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

class PDF(FPDF):
    def header(self):
        pass
    def footer(self):
        self.set_y(-12)
        self.set_font("dv", "", 7.5)
        self.set_text_color(*GREY)
        self.cell(self.epw/2, 6, "SketchUp Plugins — Οδηγός Γραφείου · SketchUp 2026", align="L")
        self.cell(self.epw/2, 6, f"σελ. {self.page_no()}", align="R")

pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(True, margin=16)
pdf.add_font("dv", "", FREG)
pdf.add_font("dv", "B", FBLD)
pdf.set_margins(14, 12, 14)
pdf.add_page()
EPW = pdf.epw  # effective page width

def h1(txt):
    pdf.set_font("dv", "B", 19); pdf.set_text_color(*PRIMARY)
    pdf.cell(0, 9, txt, new_x="LMARGIN", new_y="NEXT")

def sub(txt):
    pdf.set_font("dv", "", 10); pdf.set_text_color(*GREY)
    pdf.cell(0, 5.5, txt, new_x="LMARGIN", new_y="NEXT")

def h2(txt):
    pdf.ln(3)
    pdf.set_font("dv", "B", 13); pdf.set_text_color(*PRIMARY)
    pdf.cell(0, 7, txt, new_x="LMARGIN", new_y="NEXT")
    y = pdf.get_y()
    pdf.set_draw_color(*PRIMARY); pdf.set_line_width(0.5)
    pdf.line(pdf.l_margin, y, pdf.l_margin + EPW, y)
    pdf.ln(2)

def h3(txt):
    pdf.ln(1)
    pdf.set_font("dv", "B", 10.5); pdf.set_text_color(*ORANGE)
    pdf.cell(0, 5.5, txt, new_x="LMARGIN", new_y="NEXT")

def para(txt, size=9.5, color=DARK):
    pdf.set_font("dv", "", size); pdf.set_text_color(*color)
    pdf.multi_cell(0, 4.6, txt, new_x="LMARGIN", new_y="NEXT")

def band(txt, bg, bar, size=9.5):
    """Έγχρωμο κουτί με κάθετη μπάρα αριστερά."""
    pdf.ln(1)
    x0, y0 = pdf.get_x(), pdf.get_y()
    pdf.set_font("dv", "", size); pdf.set_text_color(*DARK)
    # μέτρηση ύψους
    lines = pdf.multi_cell(EPW - 6, 4.6, txt, dry_run=True, output="LINES")
    h = len(lines) * 4.6 + 4
    pdf.set_fill_color(*bg); pdf.rect(x0, y0, EPW, h, "F")
    pdf.set_fill_color(*bar); pdf.rect(x0, y0, 1.6, h, "F")
    pdf.set_xy(x0 + 4, y0 + 2)
    pdf.multi_cell(EPW - 6, 4.6, txt, new_x="LMARGIN", new_y="NEXT")
    pdf.set_y(y0 + h + 1)

HEAD = FontFace(color=(255,255,255), fill_color=PRIMARY, emphasis="BOLD", size_pt=8.5)
def vf(color): return FontFace(color=color, emphasis="BOLD")

# ===================== ΠΕΡΙΕΧΟΜΕΝΟ =====================
h1("SketchUp Plugins — Οδηγός Γραφείου")
sub("Πρακτικός οδηγός για αρχιτέκτονες · SketchUp 2026 · Έκδοση 2026")
pdf.ln(1)
band("Η χρυσή αρχή:  Πρώτα υγιεινή μοντέλου → μετά ταχύτητα → τελευταία οπτικοποίηση. "
     "Μην εγκαθιστάτε 20 plugins την πρώτη μέρα. Βάζουμε plugin μόνο εκεί που το native SketchUp "
     "αποτυγχάνει ή είναι πολύ αργό. Λίγα, επαληθευμένα εργαλεία — πάνω σε πραγματικό αρχείο γραφείου.",
     LIGHT, PRIMARY)

h2("1. Το πλάνο σε 3 επίπεδα")
with pdf.table(col_widths=(20,42,38), text_align=("LEFT","LEFT","LEFT"),
               line_height=5, headings_style=HEAD,
               borders_layout="MINIMAL", cell_fill_color=ROW, cell_fill_mode="ROWS") as t:
    r=t.row(); r.cell("Επίπεδο"); r.cell("Plugins"); r.cell("Σκοπός")
    r=t.row(); r.cell("Minimum\n(Day 1 · δωρεάν)"); r.cell("TT_Lib² → CleanUp³ → Solid Inspector²"); r.cell("Καθαρά, σταθερά, ελαφριά αρχεία. Μηδέν κόστος, άμεσο κέρδος.")
    r=t.row(); r.cell("Recommended\n(καθημερινή παραγωγή)"); r.cell("+ Profile Builder 4, FlexTools Pro, ΕΝΑΣ renderer (D5/Enscape/V-Ray), Architextures"); r.cell("Γρήγορη παραγωγή μελετών & κατασκευαστικών, υλικά, παρουσιάσεις.")
    r=t.row(); r.cell("Advanced\n(visualization/landscape)"); r.cell("+ Joint Push Pull/Curviloft, Skatter 2, PlaceMaker, Skimp, Quantifier Pro, Artisan 2"); r.cell("Σύνθετες επιφάνειες, περιβάλλον χώρου, βαριά assets, μετρήσεις.")
band("Τι διδάσκουμε ΠΡΩΤΑ:  τη ροή DWG → CleanUp³ → Solid Inspector² → Profile Builder 4. "
     "Όταν δουν τον τοίχο 3 στρώσεων να γίνεται σε δευτερόλεπτα, υιοθετούν τη νέα ροή.", OKBG, GREEN)

h2("2. Τα βασικά εργαλεία με μια ματιά")
rows = [
 ("TT_Lib²","Βιβλιοθήκη-υπόβαθρο (όχι UI)","Δωρεάν","Ναι","Essential",GREEN,"Εγκατάσταση ΠΡΩΤΗ, πριν το CleanUp³."),
 ("CleanUp³","Purge, καθάρισμα, μείωση μεγέθους","Δωρεάν","Ναι","Essential",GREEN,"Απαιτεί TT_Lib². Τρέξε σε αντίγραφο."),
 ("Solid Inspector²","Διόρθωση γεωμετρίας/στερεών","Δωρεάν","Πιθανό**","Essential",GREEN,"Αυτόνομο. Τρέξε πριν export/render."),
 ("Profile Builder 4","Παραμετρικοί τοίχοι, προφίλ, κιγκλιδώματα","~$119 perp.","Ναι","Essential",GREEN,"Το explode χάνει την παραμετρικότητα."),
 ("FlexTools Pro","Δυναμικά κουφώματα + WallCutter","~€99/έτος","Ναι","Recommended",ORANGE,"Όχι trial· 30-day money-back. Subscription."),
 ("Architextures","Seamless παραμετρικά υλικά","Ext. δωρεάν","Ναι","Useful",ORANGE,"Εμπορική χρήση → Pro (~£66/έτος). Internet."),
 ("Joint Push Pull","Push/Pull σε καμπύλες όψεις","~$12/$40","Ναι","Optional",GREY,"Θέλει LibFredo6 ≥15.3 + SketchUcation License."),
 ("Curviloft","Loft/skinning από contours","~$12/$40","Verify**","Optional",GREY,"Ίδιο license model με Joint Push Pull."),
 ("Skimp","Import + μείωση πολυγώνων","Perp./sub","Ναι","Optional",GREY,"Επιθετική μείωση → καταστροφή UV."),
 ("Skatter 2","Διασπορά βλάστησης/entourage","€149 / €99 έτ.","Ναι","Optional",GREY,"Χρήση Render-Only, αλλιώς κολλάει."),
 ("PlaceMaker","Site context (terrain, 3D κτίρια)","Credits/~$109 έτ.","Verify**","Optional",GREY,"Εξαρτάται από εξωτερικά δεδομένα."),
 ("Quantifier Pro","Προμετρήσεις & κοστολόγηση","~€79 perp.","Verify**","Optional",GREY,"Bundle με Profile Builder (έκπτωση)."),
 ("Artisan 2","Οργανικά/subdivision/terrain","~$99/έτος","Ναι**","Optional",GREY,"Το v2 αντικαθιστά το παλιό του 2011. Βαρύ."),
 ("1001bit Tools","Σκάλες, στέγες, περσίδες","Free/Pro ~$48","Stale","Test first",RED,"LEGACY (τελ. build 2022). Μη-παραμετρικό."),
]
with pdf.table(col_widths=(15,23,13,9,14,26), line_height=4.4,
               headings_style=HEAD, borders_layout="MINIMAL",
               cell_fill_color=ROW, cell_fill_mode="ROWS",
               text_align=("LEFT","LEFT","LEFT","CENTER","LEFT","LEFT")) as t:
    r=t.row()
    for hd in ("Plugin","Τι κάνει","Κόστος*","SU26","Verdict","Προσοχή"): r.cell(hd)
    for name,use,cost,su,verd,vc,risk in rows:
        r=t.row()
        r.cell(name, style=FontFace(emphasis="BOLD"))
        r.cell(use); r.cell(cost); r.cell(su)
        r.cell(verd, style=vf(vc)); r.cell(risk)
para("* Όλες οι τιμές ενδεικτικές — επιβεβαιώστε live πριν την αγορά.   ** Η ένδειξη «SketchUp 2026» "
     "δεν είναι 100% επιβεβαιωμένη στη σελίδα του developer — ελέγξτε ότι λέει ρητά «SketchUp 2026» στο "
     "Extension Warehouse πριν εγκαταστήσετε.", 7.6, GREY)

# ---- σελίδα 2 ----
pdf.add_page()
h2("3. Rendering — διάλεξε ΕΝΑ (έλεγξε πρώτα το hardware!)")
band("Κανόνας #1:  Rendering χωρίς έλεγχο κάρτας γραφικών & VRAM = crashes. Πρώτα μάζεψε τα specs των "
     "μηχανημάτων (GPU, VRAM, Windows/Mac, Intel ή Apple Silicon). Διαλέγουμε ΜΙΑ engine — όχι τρεις μαζί.",
     WARNBG, RED)
with pdf.table(col_widths=(20,14,22,22,18,32), line_height=4.6,
               headings_style=HEAD, borders_layout="MINIMAL",
               cell_fill_color=ROW, cell_fill_mode="ROWS",
               text_align=("LEFT","CENTER","LEFT","LEFT","LEFT","LEFT")) as t:
    r=t.row()
    for hd in ("Engine","SU 2026","Δωρεάν;","Mac;","GPU","Σημείωση"): r.cell(hd)
    data=[
     ("D5 Render","Ναι","Ναι (Community)","Όχι (Win only)","RTX 3060 Ti+","Δωρεάν tier = non-commercial. Pro ~$360/έτος."),
     ("Enscape","Ναι (4.13+)","Όχι (~$575/έτ.)","Ναι (Apple Silicon)","4GB min, 8GB+ RTX","Real-time, εύκολα walkthroughs."),
     ("V-Ray 7","Ναι","Όχι (~$540/έτ.)","Ναι (Metal)","RTX για GPU mode","Περιλαμβάνεται στο SketchUp Studio (Win)."),
     ("SketchUp Diffusion","Ναι (ext.)","Όχι (Go/Pro/Studio + credits)","Ναι (cloud)","—","Γρήγορα concept visuals. 5 credits/εικόνα."),
    ]
    for row in data:
        r=t.row()
        r.cell(row[0], style=FontFace(emphasis="BOLD"))
        for c in row[1:]: r.cell(c)
band("Σύσταση:  Windows + καλή κάρτα & μηδέν κόστος → D5.   Mac ή ομαλά walkthroughs → Enscape.   "
     "Top φωτορεαλισμός με Studio → V-Ray.   Diffusion για γρήγορο «σκίτσο» ιδέας.", LIGHT, PRIMARY)

h2("4. Τι κάνει ΗΔΗ native το SketchUp 2026 (μην βάζετε περιττά plugins)")
para("• Solid Tools — Union, Subtract, Trim, Intersect (boolean χωρίς plugin).")
para("• Sandbox Tools — βασικό terrain από ισοϋψείς.")
para("• Section Fills — γεμισμένες τομές, native από SketchUp 2024.")
para("• Overlays — live πληροφορία στο viewport (από SketchUp 2023).")
band("Κανόνας:  Επίπεδη επιφάνεια → native Push/Pull.  Boolean → Solid Tools.  Απλό έδαφος → Sandbox.  "
     "Plugin μόνο όταν αυτά δεν φτάνουν.", WARNBG, RED)

h2("5. Παγίδες & κανόνες γραφείου")
para("• Legacy: το 1001bit Tools είναι χρήσιμο αλλά δεν ενημερώνεται από το 2022 → «test before use», όχι core.")
para("• Άδειες Fredo6: πληρωμένες + κλειδώνουν σε λογαριασμό SketchUcation → κεντρική διαχείριση από IT.")
para("• LibFredo6 πρώτη: εγκατάσταση βιβλιοθήκης πριν τα Fredo6 tools, μετά restart. Λάθος έκδοση = #1 αιτία αποτυχίας.")
para("• Πηγές: μόνο Extension Warehouse / SketchUcation — ποτέ rbz από ανεπίσημα blogs.")
para("• Subscriptions: αν λήξουν (FlexTools, Architextures, renderers), σταματά η δυναμική επεξεργασία / εμπορική χρήση.")

h2("6. Σειρά εγκατάστασης (Day 1 checklist)")
band("1) TT_Lib²  →  2) CleanUp³  →  3) Solid Inspector²  →  4) (με budget) Profile Builder 4  →  "
     "5) FlexTools Pro  →  6) ένας renderer ΜΕΤΑ τον έλεγχο hardware.", OKBG, GREEN)

h2("7. Τρεις πρακτικές ασκήσεις")
h3("Άσκηση 1 — Αρχάριος: «Διάσωση μοντέλου»")
para("Βαρύ/βρόμικο εισαγόμενο μοντέλο → αντίγραφο → CleanUp³ (συντηρητικά) → Solid Inspector² στο κέλυφος → "
     "διόρθωση.  Στόχος: μείωση μεγέθους > 50%.")
h3("Άσκηση 2 — Μεσαίος: «Παραμετρική όψη»")
para("Από 2D κάνναβο → Profile Builder 4 (τοίχος + περσίδες) → 3 παράθυρα με FlexTools → αλλαγή ύψους ορόφου "
     "και επιβεβαίωση ότι όλα προσαρμόζονται μόνα τους.")
h3("Άσκηση 3 — Πραγματικό γραφείο: «Από DWG σε παρουσίαση»")
para("DWG κάτοψη → τοίχοι με Profile Builder → ανοίγματα με FlexTools WallCutter → υλικά με Architextures → "
     "τελικό CleanUp³ → ένα render (αφού ελεγχθεί το hardware).")

pdf.ln(3)
pdf.set_draw_color(*BORDER); pdf.set_line_width(0.2)
pdf.line(pdf.l_margin, pdf.get_y(), pdf.l_margin+EPW, pdf.get_y()); pdf.ln(1)
para("Τεκμηριωμένο υλικό, διασταυρωμένο από επίσημες πηγές (Extension Warehouse, help.sketchup.com, developer "
     "sites, SketchUcation, Chaos, D5) — Ιούνιος 2026. Οι τιμές/εκδόσεις αλλάζουν: επιβεβαιώστε live πριν από "
     "αγορά ή παρουσίαση.", 7.6, GREY)

out = "/home/user/davle-factory-skills/sketchup-plugins-training/SketchUp-Plugins-Odigos-Grafeiou.pdf"
pdf.output(out)
print("OK:", out)
