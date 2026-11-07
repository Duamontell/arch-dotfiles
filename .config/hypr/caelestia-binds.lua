-- ============================================
-- CAELESTIA-SPECIFIC BINDS
-- ============================================

local vars = require("variables")

local mainMod = vars.mainMod

-- launcher
hl.bind(mainMod .. " + SPACE", hl.dsp.global("caelestia:launcher"))

-- Session / Lock
hl.bind("CTRL + ALT + DELETE", hl.dsp.global("caelestia:session"))
hl.bind(mainMod .. " + L", hl.dsp.global("caelestia:lock"))

-- Sidebar / Panels
hl.bind(mainMod .. " + N", hl.dsp.global("caelestia:sidebar"))
hl.bind(mainMod .. " + K", hl.dsp.global("caelestia:showall"))

-- Screenshots
hl.bind("Print", hl.dsp.exec_cmd("caelestia screenshot"))
hl.bind(mainMod .. " + SHIFT + S", hl.dsp.global("caelestia:screenshotFreeze"))
hl.bind(mainMod .. " + SHIFT + ALT + S", hl.dsp.global("caelestia:screenshot"))
