# HON1000 Innføring, nettside

Scrolleside på nynorsk som formidlar innhaldet i `01_introduksjon_2026.key`
(første forelesing i HON1000, 26. august 2026) med juletema: blinkande lyslenkje,
snøfall, store bilete og annonseplassar med plasshaldarar for UiO Honours.

## Filer

- `index.html`: heile sida (HTML, CSS og JS i éi fil). Bileta blir henta frå `img/`.
- `img/`: optimaliserte bilete henta ut frå Keynote-fila (JPEG/PNG, maks 1600 px).
- `build_single.py`: byggjer `dist/hon1000-innforing.html`, ein einfils-versjon
  der alle bileta er innbakte som data-URI-ar (ca. 7 MB). Praktisk for deling
  som éi fil eller for Claude Artifacts (`dist/artifact.html`).

## Publisering

Mappa kan leggjast rett ut på Netlify, GitHub Pages eller UiO-webben:
last opp `index.html` og `img/`. Skriftene (Bodoni Moda, Nunito Sans,
IBM Plex Mono) blir henta frå Google Fonts.

## Annonseplassar

Tre slag plasshaldarar, alle merkte «Annonse» i koden:

- `.ad--leader` (728 × 90) under heroen
- `.ad--box` (300 × 250) mellom delane, to stader
- `.ad--tall` (300 × 600) i sidespalta ved historiedelen (vist frå 1240 px breidd)

Byt ut innhaldet i `<aside class="ad ...">` med ekte annonsekode når det er klart.

## Tilpassing

- Fargar og skrifter ligg som CSS-variablar øvst i `<style>` i `index.html`.
- Lysa blir bygde av JS (`buildLights`) og tilpassar seg breidda på vindauget.
- `prefers-reduced-motion` skrur av blinking, snø og innfasing.
