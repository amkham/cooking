
let count = 0

function plus()
{
    count +=1;
    document.getElementById('dishes-count-id').innerHTML = count;
}

function minus() {

    if(count !==0)
    {
        count -=1;
        document.getElementById('dishes-count-id').innerHTML = count;
    }

}