from dominate.tags import *
from dominate.util import raw


def section_abstract():
    h3("Abstract")
    p(
        raw(
            """
            Accent normalization aims to convert foreign-accented speech into native-like speech while preserving the speaker characteristics. In this article, we present an accent normalization pipeline that employs self-supervised discrete tokens and non-parallel training data for the conversion process. This process involves extracting input tokens from the source accented speech and passing them to the conversion model, which subsequently synthesizes the converted tokens into speech using a flow matching-based generative model. Subjective evaluations on Chinese-accent English show that our proposed method outperforms the baseline in terms of speech naturalness and reduction of accentedness, while also achieving fair timbre preservation. Moreover, we investigate two methods for controlling the total duration, which are suitable for applications like dubbing. Subjective evaluations indicate a preference for the direct duration-scaling method.
            """
        ),
        _class="lead",
    )
