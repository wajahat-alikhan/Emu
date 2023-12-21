EVA_IMAGE_SIZE = 448
OPENAI_DATASET_MEAN = (0.48145466, 0.4578275, 0.40821073)
OPENAI_DATASET_STD = (0.26862954, 0.26130258, 0.27577711)

DEFAULT_IMAGE_FILE_SUFFIX = ['jpg', '0.png', 'png', 'jpeg', 'webp']
DEFAULT_TEXT_FILE_SUFFIX = ['txt', '0.txt']

IGNORE_INDEX = -100

# special tokens
# START 
DEFAULT_PAD_TOKEN = "[PAD]"
DEFAULT_BOS_TOKEN = '<s>'
DEFAULT_EOS_TOKEN = '</s>'
DEFAULT_UNK_TOKEN = "<unk>"

DEFAULT_IMG_TOKEN = "[IMG]"
DEFAULT_IMG_END_TOKEN = "[/IMG]"
DEFAULT_IMAGE_TOKEN = "<image>"
DEFAULT_gIMG_TOKEN = "[gIMG]"
DEFAULT_gIMG_END_TOKEN = "[/gIMG]"
DEFAULT_EOC_TOKEN = "[EOC]"
DEFAULT_VIDEO_TOKEN = "[VIDEO]"

GRD_SYMBOL="<grounding>"
BOP_SYMBOL="<phrase>"
EOP_SYMBOL="</phrase>"
BOO_SYMBOL="<object>"
EOO_SYMBOL="</object>"
DOM_SYMBOL="</delimiter_of_multi_objects/>"

REC_SYMBOL="<REC>"

USER_TOKEN = "[USER]"
ASSISTANT_TOKEN = "[ASSISTANT]"
# END

DEFAULT_IMG_PLACEHOLDER = "[<IMG_PLH>]"
DEFAULT_VID_PLACEHOLDER = "[<VID_PLH>]"
FAKE_VIDEO_END_TOKEN = "[/VIDEO]"
