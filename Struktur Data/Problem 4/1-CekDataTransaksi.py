import re

def extrak_trx_id(text) :
    pattern ='#[0-9]{5,5}'
    hasil = str(re.findall(pattern, text)).replace("['#", '').replace("']", '')
    return hasil
def extrak_ns(text) :
    pattern = 'SN:[0-9]{20,20}'
    hasil = re.findall(pattern, text)
    if len(hasil) == 0 :
        return 'none'
    else :
        hasil = str(re.findall(pattern, text)).replace("['SN:", '').replace("']", '')
        return hasil
def extrak_order_id(text) :
    pattern = '[A-Z]{6,6}-[a-z|A-Z]{1,}-[0-9]{5,5}'
    hasil = str(re.findall(pattern, text)).replace("['", '').replace("']", '')
    return hasil
def extrak_no_ref(text) :
    pattern = 'Ref ld. :[0-9]{1,}'
    hasil = re.findall(pattern, text)
    if len(hasil) < 1 :
        return 'none'
    else :
        return str(hasil).replace("['Ref ld. :", '').replace("']", '')

    # hasil = str(re.findall(pattern, text)).replace("['", '').replace("']", '')

def cekDataTransaksi(list_trx) :
    # for i in list_trx :
    res = {}
    list_trx_str = str(list_trx)

    res['id_transaksi'] = extrak_trx_id(list_trx_str)
    # return id_transaksi
    res['nomor_seri'] = extrak_ns(list_trx_str)

    res['id_order'] = extrak_order_id(list_trx_str)

    res['ref_id'] = extrak_no_ref(list_trx_str)
    if res['nomor_seri'] == 'none' and res['ref_id'] == 'none' :
        res['success'] = 'False'
    else :
        res['success'] = 'True'

    return res


print(cekDataTransaksi([
    'Insert Transaction #14879',
    'Update Status To Pending Payment With Deposit',
    'Transaction Paid trx id = YPSTRX-lndragirillDG-14879',
    'Transaction On Biller type_modem arg: telkomsel mobile queue name arg: smtel-banyumas_mobile',
    'Success Manual SN:94309403940394039403 Ref ld. :394039403'
    ]))

print(cekDataTransaksi([
    'Insert Transaction #18254',
    'Update Status To Pending Payment With Deposit',
    'Transaction Paid trx id = YPSTRX-BrebeslBYS-18254',
    'Transaction On Biller type_modem arg: telkomsel mobile queue name arg: smtel-banyumas_mobile',
    'Trx. Cancel Process Begin I cancel trx with id18254',
    'Sukses Refunded trx id. 18254 with Wallet hash #ek0827p7rk89m456'
]))