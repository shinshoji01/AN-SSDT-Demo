from dominate.tags import *


systems = [
    ("Source", "source", "{spk}_{sid}.wav"),
    # ("Pseudo-target", "pseudo", "{spk}_{sid}.wav"),
    # ("Re-synthesis", "resynth", "{spk}_{sid}.resynth.wav"),
    ("Baseline", "baseline", "{spk}_{sid}-converted.wav"),
    # ("Proposed", "ours", "{spk}_{sid}.gen.wav"),
    ("Proposed w/ dur. scaling", "ours-scale", "{spk}_{sid}.gen.wav"),
    ("Proposed w/ dur. control", "ours-control-scale", "{spk}_{sid}.gen.wav"),
]

samples = [
    (
        "BWC",
        "arctic_a0368",
        "I just do appreciate it without being able to express my feelings.",
    ),
    (
        "LXC",
        "arctic_a0017",
        "From that moment his friendship for Belize turns to hatred and jealousy.",
    ),
    (
        "NCC",
        "arctic_a0084",
        "Scarcely had he uttered the name when Pierre's closing eyes shot open.",
    ),
    (
        "TXHC",
        "arctic_b0407",
        "Of course much grumbling went on, and little outbursts were continually occurring.",
    ),
    (
        "BWC",
        "arctic_a0084",
        "Scarcely had he uttered the name when Pierre's closing eyes shot open.",
    ),
    (
        "LXC",
        "arctic_b0487",
        "After all superfluous flesh is gone what is left is stringy and resistant.",
    ),
    (
        "NCC",
        "arctic_b0407",
        "Of course much grumbling went on, and little outbursts were continually occurring.",
    ),
    (
        "TXHC",
        "arctic_b0450",
        "To my dearest and always appreciated friend, I submit myself.",
    ),
]


def get_table(
    root: str = "./samples",
    control_width_px=240,
) -> html_tag:
    _div = div(cls="table-responsive", style="overflow-x: scroll").add(
        table(cls="table table-sm")
    )
    with _div:
        with thead():
            with tr():
                th("Speaker", scope="col")
                for spk, _, _ in samples:
                    th(spk, scope="col")
        with tbody():
            with tr():
                th(
                    "Text",
                    scope="row",
                    style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                )
                for _, _, text in samples:
                    td(p(text))

            for sys_name, sys_id, fname_pattern in systems:
                with tr():
                    th(
                        sys_name,
                        scope="row",
                        style="white-space: nowrap; position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                    )
                    for spk, key, _ in samples:
                        fname = fname_pattern.format(spk=spk, sid=key)
                        td(
                            audio(
                                source(
                                    src=f"{root}/{sys_id}/{fname}",
                                    type="audio/wav",
                                ),
                                controls="",
                                style=f"width: {control_width_px:d}px",
                                preload="none",
                            )
                        )
    return _div
