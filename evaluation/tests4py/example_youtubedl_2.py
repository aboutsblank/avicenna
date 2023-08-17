import string
from typing import Union, Callable

from isla.language import ISLaUnparser
from fuzzingbook.Grammars import srange

from avicenna import Avicenna
from avicenna.oracle import OracleResult
from avicenna.input import Input
from avicenna_formalizations.tests4py import (
    setup_tests4py_project,
    DEFAULT_WORK_DIR,
    construct_oracle,
    run_oracle_check,
    get_tests4py_feature_learner
)


grammar = {
    "<start>": ["<string>"],
    "<string>": ["<string_char>", "<string_char><string>"],
    "<string_char>": ["<html>", "<char>", "<and_char>", "<semi_colon>", "<hashtag>"],
    "<html>": ["<html_with_num>", "<html_and>"],
    "<and_char>": ["&"],
    "<semi_colon>": [";"],
    "<hashtag>": ["#"],
    "<char>": srange(string.ascii_letters + string.digits + "_"),
    "<html_with_num>": [
        "&#914;",
        "&#915;",
        "&#916;",
        "&#917;",
        "&#918;",
        "&#919;",
        "&#920;",
        "&#921;",
        "&#922;",
        "&#923;",
        "&#924;",
        "&#925;",
        "&#926;",
        "&#927;",
        "&#928;",
        "&#929;",
        "&#931;",
        "&#932;",
        "&#933;",
        "&#934;",
        "&#935;",
        "&#936;",
        "&#937;",
        "&#945;",
        "&#946;",
        "&#947;",
        "&#948;",
        "&#949;",
        "&#950;",
        "&#951;",
        "&#952;",
        "&#953;",
        "&#954;",
        "&#955;",
        "&#956;",
        "&#957;",
        "&#958;",
        "&#959;",
        "&#960;",
        "&#961;",
        "&#962;",
        "&#963;",
        "&#964;",
        "&#965;",
        "&#966;",
        "&#967;",
        "&#968;",
        "&#969;",
        "&#977;",
        "&#978;",
        "&#982;",
        "&nbsp;",
        "&#33;",
        "&#34;",
        "&#35;",
        "&#36;",
        "&#37;",
        "&#38;",
        "&#39;",
        "&#40;",
        "&#41;",
        "&#42;",
        "&#43;",
        "&#44;",
        "&#45;",
        "&#46;",
        "&#47;",
        "&#48;",
        "&#49;",
        "&#50;",
        "&#51;",
        "&#52;",
        "&#53;",
        "&#54;",
        "&#55;",
        "&#56;",
        "&#57;",
        "&#58;",
        "&#59;",
        "&#60;",
        "&#61;",
        "&#62;",
        "&#63;",
        "&#64;",
        "&#65;",
        "&#66;",
        "&#67;",
        "&#68;",
        "&#69;",
        "&#70;",
        "&#71;",
        "&#72;",
        "&#73;",
        "&#74;",
        "&#75;",
        "&#76;",
        "&#77;",
        "&#78;",
        "&#79;",
        "&#80;",
        "&#81;",
        "&#82;",
        "&#83;",
        "&#84;",
        "&#85;",
        "&#86;",
        "&#87;",
        "&#88;",
        "&#89;",
        "&#90;",
        "&#91;",
        "&#92;",
        "&#93;",
        "&#94;",
        "&#95;",
        "&#96;",
        "&#97;",
        "&#98;",
        "&#99;",
        "&#100;",
        "&#101;",
        "&#102;",
        "&#103;",
        "&#104;",
        "&#105;",
        "&#106;",
        "&#107;",
        "&#108;",
        "&#109;",
        "&#110;",
        "&#111;",
        "&#112;",
        "&#113;",
        "&#114;",
        "&#115;",
        "&#116;",
        "&#117;",
        "&#118;",
        "&#119;",
        "&#120;",
        "&#121;",
        "&#122;",
        "&#123;",
        "&#124;",
        "&#125;",
        "&#126;",
        "&#338;",
        "&#339;",
        "&#352;",
        "&#353;",
        "&#376;",
        "&#402;",
        "&#710;",
        "&#732;",
        "&#8194;",
        "&#8195;",
        "&#8201;",
        "&#8204;",
        "&#8205;",
        "&#8206;",
        "&#8207;",
        "&#8211;",
        "&#8212;",
        "&#8216;",
        "&#8217;",
        "&#8218;",
        "&#8220;",
        "&#8221;",
        "&#8222;",
        "&#8224;",
        "&#8225;",
        "&#8226;",
        "&#8230;",
        "&#8240;",
        "&#8242;",
        "&#8243;",
        "&#8249;",
        "&#8250;",
        "&#8254;",
        "&#8364;",
        "&#8482;",
        "&#8592;",
        "&#8593;",
        "&#8594;",
        "&#8595;",
        "&#8596;",
        "&#8629;",
        "&#8968;",
        "&#8969;",
        "&#8970;",
        "&#8971;",
        "&#9674;",
        "&#9824;",
        "&#9827;",
        "&#9829;",
        "&#9830;",
    ],
    "<html_and>": [
        "&OElig;",
        "&oelig;",
        "&Scaron;",
        "&scaron;",
        "&Yuml;",
        "&fnof;",
        "&circ;",
        "&tilde;",
        "&ensp;",
        "&emsp;",
        "&thinsp;",
        "&zwnj;",
        "&zwj;",
        "&lrm;",
        "&rlm;",
        "&ndash;",
        "&mdash;",
        "&lsquo;",
        "&rsquo;",
        "&sbquo;",
        "&ldquo;",
        "&rdquo;",
        "&bdquo;",
        "&dagger;",
        "&Dagger;",
        "&bull;",
        "&hellip;",
        "&permil;",
        "&prime;",
        "&Prime;",
        "&lsaquo;",
        "&rsaquo;",
        "&oline;",
        "&euro;",
        "&trade;",
        "&larr;",
        "&uarr;",
        "&rarr;",
        "&darr;",
        "&harr;",
        "&crarr;",
        "&lceil;",
        "&rceil;",
        "&lfloor;",
        "&rfloor;",
        "&loz;",
        "&spades;",
        "&clubs;",
        "&hearts;",
        "&diams;",
        "&Alpha;",
        "&Beta;",
        "&Gamma;",
        "&Delta;",
        "&Epsilon;",
        "&Zeta;",
        "&Eta;",
        "&Theta;",
        "&Iota;",
        "&Kappa;",
        "&Lambda;",
        "&Mu;",
        "&Nu;",
        "&Xi;",
        "&Omicron;",
        "&Pi;",
        "&Rho;",
        "&Sigma;",
        "&Tau;",
        "&Upsilon;",
        "&Phi;",
        "&Chi;",
        "&Psi;",
        "&Omega;",
        "&alpha;",
        "&beta;",
        "&gamma;",
        "&delta;",
        "&epsilon;",
        "&zeta;",
        "&eta;",
        "&theta;",
        "&iota;",
        "&kappa;",
        "&lambda;",
        "&mu;",
        "&nu;",
        "&xi;",
        "&omicron;",
        "&pi;",
        "&rho;",
        "&sigmaf;",
        "&sigma;",
        "&tau;",
        "&upsilon;",
        "&phi;",
        "&chi;",
        "&psi;",
        "&omega;",
        "&thetasym;",
        "&upsih;",
        "&piv;",
    ],
}


failing_list = [
    "&a&quot;",
    "&a&eacute;",
    "&anna&&eacute;ric",
    "&anna&#47;&eacute;ric",
    "&&#47;",
    "&&#x2F;",
    "&&period;",
    "&&apos;",
    "&&apos;&period;",
    "&period;&&apos;",
]


passing_list = [
    "&#33;",
    "&tau;&lambda;",
    "&#47;",
    "&eacute;",
    "&#2013266066;",
    "&period;&apos;",
    "&eacute;ric",
    "&period;",
    "&apos;",
    "&zeta;",
]


initial_inputs = failing_list + passing_list


if __name__ == "__main__":
    project_name: str = "youtubedl"
    bug_id: int = 3
    work_dir = DEFAULT_WORK_DIR
    setup_tests4py_project(project_name, bug_id, work_dir)

    oracle: Callable[[Union[str, Input]], OracleResult] = construct_oracle(
        project_name, bug_id, work_dir
    )

    run_oracle_check(oracle, failing_list, OracleResult.BUG)
    run_oracle_check(oracle, passing_list, OracleResult.NO_BUG)

    avicenna = Avicenna(
        grammar=grammar,
        initial_inputs=initial_inputs,
        oracle=oracle,
        max_iterations=10,
        log=True,
        feature_learner=get_tests4py_feature_learner(grammar)
    )

    diagnosis = avicenna.explain()
    print("Final Diagnosis:")
    print(ISLaUnparser(diagnosis[0]).unparse())

    print("\nEquivalent Representations:")
    for diagnosis in avicenna.get_equivalent_best_formulas():
        print(ISLaUnparser(diagnosis[0]).unparse())
