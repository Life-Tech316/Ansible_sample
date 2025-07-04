#!/usr/bin/env python
import re
from ansible.module_utils.basic import AnsibleModule

def main():
    # モジュール引数の定義。inputは必須の文字列型
    module_args = dict(
        input ={'type': 'str', 'required': True},
    )
    # AnsibleModuleオブジェクトの生成。引数仕様とチェックモード対応を指定
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    # 入力ファイルパスを取得
    input_file = module.params['input']
    # 入力ファイルを読み込みモードで開く
    with open(input_file, 'r') as file:
        html = file.read()

    # HTML内の小文字アルファベットを大文字に変換
    html = re.sub(r'[a-z]',lambda x: x.group(0).upper(), html)  

    # 変換後の内容を同じファイルに上書き保存
    with open(input_file, 'w') as file:
        file.write(html)

    # モジュールの実行結果を返す（changed=True, resultにファイル名）
    module.exit_json(changed=True, result=input_file)  

if __name__ == '__main__':
    main()
