local _0428 = (import '../spider-20190205/nl2code-0428-base.libsonnet')(output_from=true);

{
    data: _0428.data,
    model: {
        name: 'IdiomMiner',
        grammar: _0428.model.decoder_preproc.grammar,
        save_path: 'data/spider-idioms/20190513/asts'
        censor_pointers: true,
    },
}
