# pigeonium_v0
pythonでブロックチェーンっぽい通貨ネットワークを動かすやつのライブラリ

命名規則ミスったﾃﾍｯ

## Usage
```python
import pigeonium

# サーバーの選択・サーバー情報の取得
pigeonium.Config.getFromServer("https://pigeonium.h4ribote.net/server/")

# 取引の取得・検証
print(pigeonium.GET.transactions()[0].verify())

# ウォレット生成・インポート
newWallet = pigeonium.Wallet.generate()
adminWallet = pigeonium.Wallet.fromPrivate(pigeonium.Utils.hex2bytes("114514",32))

# 取引の作成・送信
newTx = pigeonium.Transaction.create(newWallet,adminWallet.address,bytes(16),100,pigeonium.GET.previousTxId())
print(newTx.toDict())
pigeonium.POST.transaction(newTx)

# 通貨発行
pigeonium.POST.issuance(pigeonium.Currency.create("YeesToken","Yees",newWallet.address),100,newWallet,adminWallet)

# APIを用いて情報(ここでは残高)を取得
print(pigeonium.GET.balance(newWallet.address))

```
