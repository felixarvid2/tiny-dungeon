"""Paths shared by the asset build modules."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))          # repository root
# The CC0 source packs live in the asset library of github.com/felixarvid2/test (its assets/ folder).
# Point TD_ASSET_LIBRARY at that folder, or clone felixarvid2/test next to this repository.
LIB = os.environ.get('TD_ASSET_LIBRARY') or os.path.join(os.path.dirname(ROOT), 'test', 'assets')
TILES_PNG = os.path.join(LIB, '2d-pixel', 'tiny-dungeon', 'Tilemap', 'tilemap_packed.png')
