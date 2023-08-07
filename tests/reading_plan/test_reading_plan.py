import pytest
from unittest.mock import Mock, patch
from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501


news_moked = [
    {
        "url": "https://blog.betrybe.com/tecnologia/jogos-iniciantes/",
        "title": "10 jogos para iniciantes aprenderem a programar!",
        "timestamp": "22/05/2023",
        "writer": "Lucas Custódio",
        "reading_time": 12,
        "summary": "A programação é o momento. De uns anos para cá.",
        "category": "Tecnologia",
    },
    {
        "url": "https://blog.betrybe.com/tecnologia/endless-os/",
        "title": "Endless OS: por que vale a pena usar esse sistema",
        "timestamp": "18/05/2023",
        "writer": "Cairo Noleto",
        "reading_time": 4,
        "summary": "Os computadores com uma configuração mais básica.",
        "category": "Tecnologia",
    },
    {
        "url": "https://blog.betrybe.com/carreira/trybetalks-nubank/",
        "title": "TrybeTalks – CTO do Nubank revela as habilidades.",
        "timestamp": "15/05/2023",
        "writer": "Lucas Custódio",
        "reading_time": 6,
        "summary": "Vitor Olivier, o CTO do Nubank.",
        "category": "Carreira",
    },
    {
        "url": "https://blog.betrybe.com/tecnologia/site-responsivo/",
        "title": "Site responsivo: o que é e 10 dicas para aplicar",
        "timestamp": "10/05/2023",
        "writer": "Lucas Marchiori",
        "reading_time": 13,
        "summary": "Com o avanço da tecnologia.",
        "category": "Tecnologia",
    },
]
group_news_result_mock_1 = {
    "readable": [
        {
            "unfilled_time": 1,
            "chosen_news": [
                (
                    "Endless OS: por que vale a pena usar esse sistema",
                    4,
                ),
                (
                    "TrybeTalks – CTO do Nubank revela as habilidades.",
                    6,
                ),
            ],
        },
    ],
    "unreadable": [
        ("10 jogos para iniciantes aprenderem a programar!", 12),
        ("Site responsivo: o que é e 10 dicas para aplicar", 13),
    ],
}
invalid_param_msg = "Valor 'available_time' deve ser maior que zero"


def test_reading_plan_group_news():
    mocked_get_news = Mock(return_value=news_moked)
    with patch("tech_news.analyzer.reading_plan.find_news", mocked_get_news):
        result = ReadingPlanService.group_news_for_available_time(11)
        with pytest.raises(ValueError,
                           match=invalid_param_msg):
            ReadingPlanService.group_news_for_available_time(-1)
        assert result == group_news_result_mock_1
