# coding:utf-8

import unittest
from pact.matchers import Matcher, Like, EachLike, Term, Enum, PactVerify


class Test(unittest.TestCase):

    # Matcher基础配置-校验通过
    def test_matcher_base_1(self):
        expected_format = Matcher({
            'code': 0,
            'msg': 'success',
        })
        result_1 = {
            'code': 0,
            'msg': 'success11',
            'data': {'name': 'Jonas', 'age': 10, 'phone': 'bbb'},
            'age_2': 'aaa'
        }

        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_1)
        print('test_matcher_base_1', mPactVerify.verify_info)
        assert mPactVerify.verify_result == True

    # Macher基础基础配置2-校验不通过
    def test_matcher_base_2(self):
        expected_format = Matcher({
            'code': 0,
            'msg': 'fail',
        })
        result_2 = [{
            'code': 0,
            'msg': 'success',
            'data': {'name': 'Jonas', 'age': 10, 'phone': 'bbb'},
            'age_2': 'aaa'
        }]
        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_2)
        ##print('test_matcher_base_2', mPactVerify.verify_info)
        assert mPactVerify.verify_result == False

    # Macher配置
    def test_matcher_base_3(self):
        expected_format = Matcher({'k1': 'v1'})
        result_2 = {
            'k1': 'v2',
            'code': 0,
            'msg': 'success',
            'data': {'name': 'Jonas', 'age': 10, 'phone': 'bbb'},
            'age_2': 'aaa'
        }
        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_2)
        ## print('test_matcher_base_3', mPactVerify.verify_info)
        assert mPactVerify.verify_result == False

    # Macher配置
    def test_matcher_base_4(self):
        expected_format = Matcher(11)
        result_2 = 'aa'
        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_2)
        ## print('test_matcher_base_4', mPactVerify.verify_info)
        assert mPactVerify.verify_result == False

    # Macher配置
    def test_matcher_base_5(self):
        expected_format = Matcher({
            'code': 0,
            'msg': 'success',
            'data': Like(
                {'name': 'Jonas11', 'age': 12, 'phone': 'bbbaa'}
            )
        })
        result_2 = {
            'code': 0,
            'msg': 'success',
            'data': {'name': 'Jonas', 'age': '11', 'phone': 'bbb'},
            'age_2': 'aaa'
        }
        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_2)
        ## print('test_matcher_base_5', mPactVerify.verify_info)
        assert mPactVerify.verify_result == False

    # Like基础配置-校验通过
    def test_like_base_1(self):
        expected_format = Like({
            'code': 0,
            'msg': 'success',
            'price': 1.0,
            'valid': True,
            'info': None,
            'info_1': [11],
            'info_2': {'k1': 'v1'}
        })
        result_1 = {
            'code': 1,
            'msg': 'haha',
            'price': 2.0,
            'valid': False,
            'info': None,
            'info_1': [1112],
            'info_2': []
        }
        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_1)
        ##print('test_like_base_1', mPactVerify.verify_info)
        assert mPactVerify.verify_result == True

    # Like配置-校验不通过
    def test_like_base_2(self):
        expected_format = Like({
            'code': 0,
            'msg': 'success',
            'price': 1.0,
            'valid': True,
            'info': None,
            'info_1': [11],
            'info_2': {'k1': 'v1'},
            'info_3': 11
        })
        result_1 = {
            'code': 1,
            'msg': 'haha',
            'price': 2.0,
            'valid': False,
            'info': None,
            'info_1': [1112],
            'info_2': 11
        }
        # # print(expected_format)
        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_1)
        # print('test_like_base_2', mPactVerify.verify_info)
        assert mPactVerify.verify_result == False

    # Like-Term嵌套-校验不通过
    def test_like_base_3(self):
        expected_format = Like({
            'code': 0,
            'msg': 'success',
            'price': 1.0,
            'valid': True,
            'info': None,
            'info_1': [11],
            'info_2': Term(r'\d{2}', 11)
        })
        result_1 = {
            'code': 1,
            'msg': 'haha',
            'price': 2.0,
            'valid': False,
            'info': None,
            'info_1': [1112],
            'info_2': 1
        }
        # # print(expected_format)
        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_1)
        ##print('test_like_base_3', mPactVerify.verify_info)
        assert mPactVerify.verify_result == False

    # Like配置,目标数据格式不符合
    def test_like_base_4(self):
        expected_format = Like({
            'code': 0,
            'msg': 'success',
            'price': 1.0,
            'valid': True,
            'info': None,
            'info_1': [11],
            'info_2': {'k1': 'v1'}
        })
        result_1 = 11
        # # print(expected_format)
        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_1)
        ## print('test_like_base_4', mPactVerify.verify_info)
        assert mPactVerify.verify_result == False

    # Like-Like嵌套
    def test_like_base_5(self):
        expected_format = Like({
            'code': 0,
            'msg': 'success',
            'price': 1.0,
            'valid': True,
            'info': None,
            'info_1': [11],
            'info_2': Like({
                "k1": 11,
                "k2": '22',
                'k3': 1.0
            })
        })
        result_1 = {
            'code': 0,
            'msg': 'success',
            'price': 1.0,
            'valid': True,
            'info': None,
            'info_1': [11],
            'info_2': {
                "k1": 11,
                "k2": 22
            }
        }
        # # print(expected_format.generate())
        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_1)
        print('test_like_base_5', mPactVerify.verify_info)
        assert mPactVerify.verify_result == False

    # Like-Like嵌套

    def test_like_base_6(self):
        expected_format = Matcher({
            "msg": "success",
            "code": 0,
            "data": Like({
                "target_user_info": Like({
                    "user_identity": 1,
                    "game_certify_info": EachLike({
                        "dict_id": 1,
                        "name": "王者荣耀",
                        "order_index": 1,
                        "url": "https://g.baojiesports.com/bps/89044cf2425d4b96b0540ee0bcc8123e-150-100.png",
                        "code": "1"
                    })
                }),
                "in_order_relation": 0,
                "order_sequence": "",
                "current_order_status": -1,
                "current_order_status_desc": "",
                "countdown": -1,
                "order_status_circulation": []
            })
        })
        result_1 = {
            "msg": "success",
            "code": 0,
            "data": {
                "target_user_info": {
                    "user_identity": 1,
                    "game_certify_info": [{
                        "dict_id": 1,
                        "name": "王者荣耀",
                        "order_index": 1,
                        "url": "https://g.baojiesports.com/bps/89044cf2425d4b96b0540ee0bcc8123e-150-100.png",
                        "code": "1"
                    }, {
                        "dict_id": 3,
                        "name": "绝地求生",
                        "order_index": 2,
                        "url": "https://g.baojiesports.com/bps/2f7e78df1ece496aa6a01df958bd7828-150-100.png",
                        "code": "3"
                    }
                    ]
                },
                "in_order_relation": 0,
                "order_sequence": "",
                "current_order_status": -1,
                "current_order_status_desc": "",
                "countdown": -1,
                "order_status_circulation": []
            }
        }
        # # print(expected_format.generate())
        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_1)
        print('test_like_base_6', mPactVerify.verify_info)
        assert mPactVerify.verify_result == True

    # Like-Matcher嵌套
    def test_like_base_7(self):
        expected_format = Like({
            'code': 0,
            'msg': 'success',
            'price': 1.0,
            'valid': True,
            'info': None,
            'info_1': [11],
            'info_2': Matcher({'k1': 'v1'}),
            'info_3': Matcher(11),
            'info_4': Matcher(11)
        })
        result_1 = {
            'code': 0,
            'msg': 'success',
            'price': 1.0,
            'valid': True,
            'info': None,
            'info_1': [11],
            'info_2': {
                "k1": 11,
                "k2": 22
            },
            'info_3': 'aa',
            'info_4': []
        }
        # # print(expected_format.generate())
        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_1)
        ## print('test_like_base_7', mPactVerify.verify_info)
        assert mPactVerify.verify_result == False

    # Term基础配置
    def test_term_base_1(self):
        expected_format = Term(r'^\d{2}$', 11)
        result_1 = 112
        # # print(expected_format.generate())
        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_1)
        ## print('test_term_base_1', mPactVerify.verify_info)
        assert mPactVerify.verify_result == True

    # EachLike单层配置
    def test_eachlike_base_1(self):
        expected_format = Like({
            'code': 0,
            'msg': 'success',
            'data': EachLike({
                "k1": 11,
                'k2': 'aa',
                'k3': 'haah'})
        })
        result_1 = {
            'code': 0,
            'msg': 'success',
            'data': [{
                "k1": 11,
                'k2': 'aa',
                'k3': True},
                {
                    "k1": 11,
                    'k2': 'aa'}
            ]
        }
        # # print(expected_format.generate())
        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_1)
        ##print('test_eachlike_base_1', mPactVerify.verify_info)
        assert mPactVerify.verify_result == False

    # EachLike多层嵌套
    def test_eachlike_base_2(self):
        expected_format = Like({
            'code': 0,
            'msg': 'success',
            'data': EachLike(EachLike({
                "k1": 11,
                'k2': 'aa',
                'k3': 'haah'}))
        })
        result_1 = {
            'code': 'aa',
            'msg': 'success',
            'data': [[{
                "k1": 11,
                'k2': 'aa',
                'k3': True}
            ], [
                {
                    "k1": 11,
                    'k2': 'aa'}
            ]]
        }
        # # print(expected_format.generate())
        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_1)
        # print('test_eachlike_base_2', mPactVerify.verify_info)
        assert mPactVerify.verify_result == False

    # EachLike-Term嵌套
    def test_eachlike_base_3(self):
        expected_format = Like({
            'code': 0,
            'msg': 'success',
            'data': EachLike(EachLike({
                "k1": 11,
                'k2': 'aa',
                'k3': Term('^\d{2}$', example=11)}))
        })
        result_1 = {
            'code': 0,
            'msg': 'success',
            'data': [[{
                "k1": 12123,
                'k2': 'aaasda',
                'k3': 123},
                {
                    "k1": 12324,
                    'k2': 'aa'}
            ], [{
                'k2': 'aa'}]]
        }
        # # print(expected_format.generate())
        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_1)
        print('test_eachlike_base_2', mPactVerify.verify_info)
        assert mPactVerify.verify_result == False

    # EachLike-len测试
    def test_eachlike_base_4(self):
        expected_format = Like({
            'code': 0,
            'msg': 'success',
            'data': EachLike({
                "k1": 11,
                'k2': 'aa',
                'k3': Term('^\d{2}$', example=11)}, minimum=3)
        })
        result_1 = {
            'code': 0,
            'msg': 'success',
            'data': []
        }
        # # print(expected_format.generate())
        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_1)
        print('test_eachlike_base_4', mPactVerify.verify_info)
        assert mPactVerify.verify_result == False

    # EachLike-len测试
    def test_eachlike_base_5(self):
        expected_format = Like({
            'code': 0,
            'msg': 'success',
            'data': EachLike({
                "k1": 11,
                'k2': 'aa',
                'k3': Term('^\d{2}$', example=11)}, minimum=1)
        })
        result_1 = {
            'code': 0,
            'msg': 'success',
            'data': [{
                "k1": 11,
                'k2': 'aa',
                'k3': '11'}]
        }
        # # print(expected_format.generate())
        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_1)
        print('test_eachlike_base_5', mPactVerify.verify_info)
        assert mPactVerify.verify_result == False

    # EachLike测试
    def test_eachlike_base_6(self):
        expected_format = EachLike({
            'user': 'lilei',
            'age': 10,
            'sex': Matcher('man')
        })
        result_1 = [{
            'user': 'lili',
            'age': 12,
            'sex': 'women'
        }]
        # # print(expected_format.generate())
        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_1)
        print('test_eachlike_base_6', mPactVerify.verify_info)
        assert mPactVerify.verify_result == False

    def test_eachlike_base_7(self):
        expected_format = EachLike(
            11
        )
        result_1 = [11, 'aa']
        # # print(expected_format.generate())
        mPactVerify = PactVerify(expected_format)
        # print(expected_format.generate())

        mPactVerify.verify(result_1)
        #print('test_eachlike_base_7', mPactVerify.verify_info)
        assert mPactVerify.verify_result == False

    def test_eachlike_base_8(self):
        expected_format = EachLike(EachLike(
            {'k1': 'v1'}
        ))
        result_1 = [[{'k1': 'v2'}]]
        # # print(expected_format.generate())
        mPactVerify = PactVerify(expected_format)
        # print(expected_format.generate())

        mPactVerify.verify(result_1)
        print('test_eachlike_base_8', mPactVerify.verify_info)
        assert mPactVerify.verify_result == True

    # EachLike最小长度允许为空
    def test_eachlike_base_9(self):
        expected_format = EachLike(
            {'k1': 'v1'}, minimum=0
        )
        result_1 = []
        # # print(expected_format.generate())
        mPactVerify = PactVerify(expected_format)
        # print(expected_format.generate())

        mPactVerify.verify(result_1)
        print('test_eachlike_base_9', mPactVerify.verify_info)
        assert mPactVerify.verify_result == True

    # EachLike最小长度允许为空
    def test_eachlike_base_10(self):
        expected_format = Matcher({
            "msg": "success",
            "code": 0,
            "data": Like({
                "basic_info": Like({
                    "game_code": 1,
                    "bj": Like({
                        "tags_strength": EachLike(EachLike({
                            "tag_id": 273,
                            "tag_name": "Carry全场",
                        }, minimum=0)),
                        "tags_service": EachLike(EachLike({
                            "tag_id": 294,
                            "tag_name": "开挂/作弊"
                        }, minimum=0)),
                        "tips_strength": EachLike("非常差！"),
                        "tips_service": EachLike("非常差！各方面都很差！")
                    }),
                    "bn": Like({
                        "tags_strength": EachLike(EachLike({
                            "tag_id": 273,
                            "tag_name": "Carry全场"
                        }, minimum=0)),
                        "tags_service": EachLike(EachLike({
                            "tag_id": 294,
                            "tag_name": "开挂/作弊"
                        }, minimum=0)),
                        "tips_strength": EachLike("非常差！"),
                        "tips_service": EachLike("非常差！各方面都很差！")
                    }),
                }),
                "baoji_info": EachLike({
                    "uid": "809c94b9",
                    "chicken_id": "87385416",
                    "username": "勇敢的暴鸡",
                    "avatar": "https://qn-bn-pub.kaiheikeji.com/baobao/defalutavatar/baobaodefalutavatar.png",
                    "sex": 1,
                    "identity": 1,
                    "baoji_level": 100,
                    "baoji_level_name": "普通暴鸡"
                })
            })
        })
        result_1 = {
            "msg": "success",
            "code": 0,
            "data": {
                "basic_info": {
                    "game_code": 1,
                    "bj": {
                        "tags_strength": [[], [], [], [], [{
                            "tag_id": 273,
                            "tag_name": "Carry全场"
                        }, {
                            "tag_id": 274,
                            "tag_name": "意识超群"
                        }, {
                            "tag_id": 287,
                            "tag_name": "制霸峡谷"
                        }
                        ]],
                        "tags_service": [[{
                            "tag_id": 294,
                            "tag_name": "开挂/作弊"
                        }, {
                            "tag_id": 293,
                            "tag_name": "恶意挂机"
                        }, {
                            "tag_id": 292,
                            "tag_name": "演员"
                        }, {
                            "tag_id": 291,
                            "tag_name": "色情骚扰"
                        }, {
                            "tag_id": 290,
                            "tag_name": "脏话连篇"
                        }, {
                            "tag_id": 289,
                            "tag_name": "言语辱骂"
                        }
                        ], [{
                            "tag_id": 294,
                            "tag_name": "开挂/作弊"
                        }, {
                            "tag_id": 293,
                            "tag_name": "恶意挂机"
                        }, {
                            "tag_id": 292,
                            "tag_name": "演员"
                        }, {
                            "tag_id": 291,
                            "tag_name": "色情骚扰"
                        }, {
                            "tag_id": 290,
                            "tag_name": "脏话连篇"
                        }, {
                            "tag_id": 289,
                            "tag_name": "言语辱骂"
                        }
                        ], [{
                            "tag_id": 295,
                            "tag_name": "态度冷淡"
                        }, {
                            "tag_id": 296,
                            "tag_name": "频繁索要好评"
                        }, {
                            "tag_id": 297,
                            "tag_name": "服务时长不足"
                        }
                        ], [{
                            "tag_id": 295,
                            "tag_name": "态度冷淡"
                        }, {
                            "tag_id": 296,
                            "tag_name": "频繁索要好评"
                        }, {
                            "tag_id": 297,
                            "tag_name": "服务时长不足"
                        }
                        ], [{
                            "tag_id": 278,
                            "tag_name": "真·声控福利"
                        }, {
                            "tag_id": 280,
                            "tag_name": "沉着冷静"
                        }, {
                            "tag_id": 279,
                            "tag_name": "电竞BB机"
                        }, {
                            "tag_id": 282,
                            "tag_name": "教学有干货"
                        }, {
                            "tag_id": 283,
                            "tag_name": "温柔"
                        }
                        ]],
                        "tips_strength": ["非常差！", "比较差", "一般，还需改善", "很不错，仍可改善", "非常好，6到飞起"],
                        "tips_service": ["非常差！各方面都很差！", "不满意，比较差", "一般，还需改善", "满意，仍可改善", "非常满意"]
                    },
                    "bn": {
                        "tags_strength": [[], [], [], [], [{
                            "tag_id": 273,
                            "tag_name": "Carry全场"
                        }, {
                            "tag_id": 274,
                            "tag_name": "意识超群"
                        }, {
                            "tag_id": 287,
                            "tag_name": "制霸峡谷"
                        }
                        ]],
                        "tags_service": [[{
                            "tag_id": 294,
                            "tag_name": "开挂/作弊"
                        }, {
                            "tag_id": 293,
                            "tag_name": "恶意挂机"
                        }, {
                            "tag_id": 292,
                            "tag_name": "演员"
                        }, {
                            "tag_id": 291,
                            "tag_name": "色情骚扰"
                        }, {
                            "tag_id": 290,
                            "tag_name": "脏话连篇"
                        }, {
                            "tag_id": 289,
                            "tag_name": "言语辱骂"
                        }
                        ], [{
                            "tag_id": 294,
                            "tag_name": "开挂/作弊"
                        }, {
                            "tag_id": 293,
                            "tag_name": "恶意挂机"
                        }, {
                            "tag_id": 292,
                            "tag_name": "演员"
                        }, {
                            "tag_id": 291,
                            "tag_name": "色情骚扰"
                        }, {
                            "tag_id": 290,
                            "tag_name": "脏话连篇"
                        }, {
                            "tag_id": 289,
                            "tag_name": "言语辱骂"
                        }
                        ], [{
                            "tag_id": 295,
                            "tag_name": "态度冷淡"
                        }, {
                            "tag_id": 296,
                            "tag_name": "频繁索要好评"
                        }, {
                            "tag_id": 297,
                            "tag_name": "服务时长不足"
                        }
                        ], [{
                            "tag_id": 295,
                            "tag_name": "态度冷淡"
                        }, {
                            "tag_id": 296,
                            "tag_name": "频繁索要好评"
                        }, {
                            "tag_id": 297,
                            "tag_name": "服务时长不足"
                        }
                        ], [{
                            "tag_id": 278,
                            "tag_name": "真·声控福利"
                        }, {
                            "tag_id": 279,
                            "tag_name": "电竞BB机"
                        }, {
                            "tag_id": 283,
                            "tag_name": "温柔"
                        }, {
                            "tag_id": 284,
                            "tag_name": "敲可爱"
                        }, {
                            "tag_id": 288,
                            "tag_name": "就很甜"
                        }, {
                            "tag_id": 285,
                            "tag_name": "峡谷御姐"
                        }
                        ]],
                        "tips_strength": ["非常差！", "比较差", "一般，还需改善", "很不错，仍可改善", "非常好，6到飞起"],
                        "tips_service": ["非常差！各方面都很差！", "不满意，比较差", "一般，还需改善", "满意，仍可改善", "非常满意"]
                    }
                },
                "baoji_info": [{
                    "uid": "809c94b9",
                    "chicken_id": "87385416",
                    "username": "勇敢的暴鸡",
                    "avatar": "https://qn-bn-pub.kaiheikeji.com/baobao/defalutavatar/baobaodefalutavatar.png",
                    "sex": 1,
                    "identity": 1,
                    "baoji_level": 100,
                    "baoji_level_name": "普通暴鸡"
                }
                ]
            }
        }

        # # print(expected_format.generate())
        mPactVerify = PactVerify(expected_format)
        # print(expected_format.generate())

        mPactVerify.verify(result_1)
        print('test_eachlike_base_10', mPactVerify.verify_info)
        assert mPactVerify.verify_result == True

    # EachLike最小长度允许为空
    def test_eachlike_base_11(self):
        expected_format = EachLike(
            {'k1': Matcher('v1')}
        )
        result_1 = [{'k1': 'v1'}, {'k1': 'v2'}]
        # # print(expected_format.generate())
        mPactVerify = PactVerify(expected_format)
        # print(expected_format.generate())

        mPactVerify.verify(result_1)
        print('test_eachlike_base_9', mPactVerify.verify_info)
        assert mPactVerify.verify_result == False

    # enum校验_1
    def test_enum_base_1(self):
        expected_format = Enum([11, 22])
        result_1 = 13

        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_1)
        print('test_enum_base_1', mPactVerify.verify_info)
        assert mPactVerify.verify_result == False

    # enum校验_2
    def test_enum_base_2(self):
        expected_format = Enum([{'k1': 'v1'}, {'k1': 'v2'}])
        result_1 = {'k1': 'v2'}

        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_1)
        print('test_enum_base_1', mPactVerify.verify_info)
        assert mPactVerify.verify_result == True

    # enum校验_3
    def test_enum_base_3(self):
        expected_format = Matcher({
            'code': 0,
            'msg': 'success',
            'age': Enum([11, 22, 33])
        })
        result_1 = {
            'code': 0,
            'msg': 'success',
            'age': 11
        }
        # print(expected_format.generate())
        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_1)
        print('test_enum_base_1', mPactVerify.verify_info)
        assert mPactVerify.verify_result == True

    # enum校验_4
    def test_enum_base_4(self):
        expected_format = Like({
            'code': 0,
            'msg': 'success',
            'age': Enum([11, 22])
        })
        result_1 = {
            'code': 0,
            'msg': 'success',
            'age': 11
        }
        # print(expected_format.generate())
        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_1)
        print('test_enum_base_1', mPactVerify.verify_info)
        assert mPactVerify.verify_result == True

    # enum校验_5
    def test_enum_base_5(self):
        expected_format = Like({
            'code': 0,
            'msg': 'success',
            'data': EachLike({'name': Enum(['liuhui', 'xiaoli'])})
        })
        result_1 = {
            'code': 0,
            'msg': 'success',
            'data': {'name': 'liuhui'}
        }
        mPactVerify = PactVerify(expected_format)
        mPactVerify.verify(result_1)
        print('test_enum_base_1', mPactVerify.verify_info)
        assert mPactVerify.verify_result == True

    #
    def test_1111(self):
        expect_format = Matcher({'k1': 'v1'})
        # 实际数据
        actual_data = {'k1': 'v2'}
        mPactVerify = PactVerify(expect_format)
        mPactVerify.verify(actual_data)
        print('test_1111', mPactVerify.verify_info)
        assert mPactVerify.verify_result == True
if __name__ == '__main__':
    unittest.main()