import os
import sys
import json
from xml.etree.ElementInclude import include

import NXOpen


def main(
        prtPath: str,
        parameters: str,  # dumped json
        x_tPath: str = None,
        include_curves: bool or None = None,  # None: same with user's last export setting
        include_surfaces: bool or None = None,  # None: same with user's last export setting
        include_solids: bool or None = None,  # None: same with user's last export setting
        flatten_assembly: bool or None = None,  # None: same with user's last export setting
):
    """Update the parameter of .prt file and export to .x_t file."""

    # 保存先の設定
    prtPath = os.path.abspath(prtPath)
    if x_tPath is None:
        x_tPath = os.path.splitext(prtPath)[0] + '.x_t'

    # 辞書の作成
    parameters = json.loads(parameters)
    
    # session の取得とパートを開く
    theSession = NXOpen.Session.GetSession()
    theSession.Parts.OpenActiveDisplay(prtPath, NXOpen.DisplayPartOption.AllowAdditional)
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")

    # part の設定
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display

    # 式を更新
    for k, v in parameters.items():
        try:
            exp = workPart.Expressions.FindObject(k)
        except NXOpen.NXException:
            print(f'├ 変数{k}は .prt ファイルに含まれていません。無視されます。')
            continue

        workPart.Expressions.Edit(exp, str(v))
        # 式の更新を適用
        id1 = theSession.NewestVisibleUndoMark
        try:
            nErrs1 = theSession.UpdateManager.DoUpdate(id1)
        # 更新に失敗
        except NXOpen.NXException as e:
            print(f'├ ERROR! {e}')
            print(f'└ 形状が破綻しました。操作を取り消します。')
            return None

    print('│ model 更新に成功しました。')

    try:
        # parasolid のエクスポート
        parasolidExporter1 = theSession.DexManager.CreateParasolidExporter()

        if include_curves is not None:
            parasolidExporter1.ObjectTypes.Curves = include_curves

        if include_surfaces is not None:
            parasolidExporter1.ObjectTypes.Surfaces = include_surfaces

        if include_solids is not None:
            parasolidExporter1.ObjectTypes.Solids = include_solids

        if flatten_assembly is not None:
            parasolidExporter1.FlattenAssembly = flatten_assembly

        parasolidExporter1.InputFile = prtPath
        parasolidExporter1.ParasolidVersion = NXOpen.ParasolidExporter.ParasolidVersionOption.Current
        parasolidExporter1.OutputFile = x_tPath

        parasolidExporter1.Commit()
        parasolidExporter1.Destroy()

    except Exception as e:
        print(f'├ ERROR! {e}')
        print(f'└ parasolid 更新に失敗しました。')
        return None

    print('└ parasolid 更新が正常に終了しました。')
    return None



if __name__ == "__main__":
    print('---NX started---')
    print('current directory: ', os.getcwd())
    print('arguments: ')
    for arg in sys.argv[1:]:
        print('│ ', arg)
    main(*sys.argv[1:])
    print('---NX end---')
