pragma solidity >=0.7.0 <0.9.0;

contract procurement {
    uint256 public job_id = 0;
    address owner;

    constructor() {
        owner = msg.sender;
    }

    struct Supplier_details {
        uint256 job_id;
        string name;
        string price_unit;
        string total_price;
        string zimraITF263;
        string praz;
        string validity;
    }

    mapping(address => Supplier_details) public supplier;

    struct Client {
        string name;
        string product_type;
        string product;
        string requirements;
        string date;
        string delivery_period;
        uint256 job;
    }

    mapping(address => Client) public transaction;

    event Jobs(
        string name,
        string product_type,
        string product,
        string requirements,
        string date,
        string delivery_period,
        uint256 job
    );

    event Bidders(
        uint256 job_id,
        string name,
        string price_unity,
        string total_price,
        string zimraITF263,
        string praz,
        string validity
    );

    event Winner(
        uint256 job_id,
        string name,
        string price_unity,
        string total_price,
        string zimraITF263,
        string praz,
        string validity
    );

    mapping(address => uint256) public user;

    function addTransaction(
        string memory _name,
        string memory _productType,
        string memory _product,
        string memory _req,
        string memory _date,
        string memory _del
    ) public {
        Client storage client = transaction[owner];
        job_id++;
        client.name = _name;
        client.product_type = _productType;
        client.product = _product;
        client.requirements = _req;
        client.date = _date;
        client.delivery_period = _del;
        client.job = job_id;

        emit Jobs(_name, _productType, _product, _req, _date, _del, job_id);
    }

    function addSuppliers(
        uint256 _job,
        string memory _supNm,
        string memory unit_price,
        string memory total_price,
        string memory _zimraITF263,
        string memory _praz,
        string memory _validity
    ) public {
        Supplier_details storage bid = supplier[owner];
        bid.job_id = _job;
        bid.name = _supNm;
        bid.price_unit = unit_price;
        bid.total_price = total_price;
        bid.zimraITF263 = _zimraITF263;
        bid.praz = _praz;
        bid.validity = _validity;

        emit Bidders(
            _job,
            _supNm,
            unit_price,
            total_price,
            _zimraITF263,
            _praz,
            _validity
        );
    }

    //setJob_id maps user to job.id for the tender
    function setJob_id(address _addr, uint256 _id) public {
        user[_addr] = _id;
    }

    // Exist() makes user to award bider only once by using user[]
    modifier Exist(uint256 _id) {
        require(user[owner] != _id, "Exist");
        _;
        setJob_id(owner, _id);
    }

    function award_bider(
        uint256 _job,
        string memory _supNm,
        string memory unit_price,
        string memory total_price,
        string memory _zimraITF263,
        string memory _praz,
        string memory _validity
    ) public Exist(_job) {
        Supplier_details storage bid = supplier[owner];
        bid.job_id = _job;
        bid.name = _supNm;
        bid.price_unit = unit_price;
        bid.total_price = total_price;
        bid.zimraITF263 = _zimraITF263;
        bid.praz = _praz;
        bid.validity = _validity;

        emit Winner(
            _job,
            _supNm,
            unit_price,
            total_price,
            _zimraITF263,
            _praz,
            _validity
        );
    }
}
