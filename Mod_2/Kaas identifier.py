geel = input('is de kaas geel? ')
if geel == 'nee':
    blauwe_schimmel  = input('heeft de kaas blauwe schimmels? ')
    if blauwe_schimmel == 'ja':
            korst_schimmel  = input('heeft de kaas een korst? ')
            if korst_schimmel == 'ja':
                print('uw kaas is blue rochbaron')
            else:
                print('uw kaas is foume d ambert')
    else:
        korst_geen_schimmel = input('heeft de kaas een korst? ')
        if korst_geen_schimmel == 'ja':
            print('uw kaas is camembert')
        else:
            print('uw kaas is mozzarella')

else:
    gaten = input('heeft de kaas gaten? ')
    if gaten == 'ja':
        duur = input('is de kaas duur? ')
        if duur == 'ja':
            print('uw kaas is emmenthaler')
        else:
            print('uw kaas is leerdammer')
    else:
        steen = input('is de kaas zo hard als steen? ')
        if steen == 'ja':
            print('uw kaas is parmiginano reggiano')
        else:
            print('uw kaas is goudse kaas')    