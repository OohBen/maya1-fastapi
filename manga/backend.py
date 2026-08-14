"""The image backend seam.

Everything else in this pipeline builds PROMPTS. This module is the only place that knows how a
prompt becomes a PNG, so a different generator can be dropped in without touching a single
chapter file.

To port to a host with its own image tool (e.g. OpenAI Codex), implement `generate()` with the
same signature and set MANGA_BACKEND=<name>. Nothing else changes.

    generate(prompt, refs, quality, size) -> (png_bytes, cost_usd)

      prompt : str          the fully-assembled page prompt
      refs   : list[str]    local file paths, fed as visual reference images, in order.
                            The prompt refers to them as "Image 1", "Image 2", ... so ORDER
                            MATTERS and must be preserved.
      quality: str          "low" | "medium" | "high". A backend with no tier control should
                            ignore this and report its own cost (0.0 if free).
      size   : str          "WIDTHxHEIGHT". Pages are 9:16 portrait: "1152x2048" or "2160x3840".

Reference images are not optional decoration — character consistency across 350+ pages depends
entirely on them. A backend that cannot accept input images will not reproduce this book.
"""
import os

BACKEND = os.environ.get("MANGA_BACKEND", "replicate")


def generate(prompt, refs=(), quality="low", size="1152x2048"):
    """Dispatch to the configured backend. Returns (png_bytes, cost_usd)."""
    if BACKEND == "replicate":
        from genlib import rep_generate
        return rep_generate(prompt, refs=refs, quality=quality, aspect=size)

    if BACKEND == "codex":
        # Implement using the host's native image tool. Contract:
        #   - pass `refs` through as input/reference images, in order
        #   - request `size` exactly; do NOT let the host pick a default aspect ratio
        #   - return raw PNG bytes and 0.0
        # See AGENTS.md, "Porting the image backend".
        raise NotImplementedError(
            "codex backend not implemented — see AGENTS.md, 'Porting the image backend'")

    raise ValueError(f"unknown MANGA_BACKEND {BACKEND!r}")
